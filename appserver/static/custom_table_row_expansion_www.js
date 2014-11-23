require([
    'splunkjs/mvc/tableview',
    'splunkjs/mvc/chartview',
    'splunkjs/mvc/searchmanager',
    'splunkjs/mvc',
    'underscore',
    'splunkjs/mvc/simplexml/ready!'],function(
    TableView,
    ChartView,
    SearchManager,
    mvc,
    _
    ){

    var EventSearchBasedRowExpansionRenderer = TableView.BaseRowExpansionRenderer.extend({
        initialize: function(args) {
            // initialize will run once, so we will set up a search and a chart to be reused.
            this._searchManager = new SearchManager({
                id: 'details-search-manager',
                preview: true
            });
            this._chartView = new ChartView({
                managerid: 'details-search-manager',
                'charting.legend.placement': 'bottom'
            });
        },

        canRender: function(rowData) {
            // Since more than one row expansion renderer can be registered we let each decide if they can handle that
            // data
            // Here we will always handle it.
            return true;
        },

        render: function($container, rowData) {
            // rowData contains information about the row that is expanded.  We can see the cells, fields, and values
            // We will find the sourcetype cell to use its value
            var sourcetypeCell = _(rowData.cells).find(function (cell) {
               return cell.field === 'site';
            });

            // Update the search's time range
            this._searchManager.set("earliest_time", "-1h");
            this._searchManager.set("latest_time", "now");

            //update the search with the sourcetype that we are interested in
            this._searchManager.set({ search: 'sourcetype="stream:http" site="' + sourcetypeCell.value + '" | timechart max(response_time) | rename max(response_time) AS "Maximum Response Time in MS" '});

            // $container is the jquery object where we can put out content.
            // In this case we will render our chart and add it to the $container
            $container.append(this._chartView.render().el);
        }
    });

    var tableElement = mvc.Components.getInstance("table1");
    tableElement.getVisualization(function(tableView) {
        tableView.addRowExpansionRenderer(new EventSearchBasedRowExpansionRenderer());
        tableView.render();
    });
});
