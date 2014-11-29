Author:  James Donn

This demo requires a few configuration updates in other Apps to work.  This doc breaks down what each dashboard requires.

### Stream Splunk HTTP and User Access Data 

This requires updates to the splunk_app_stream App.

1) To capture data from the loopback address on your Mac, place this file in local/streamfwd.xml:

<?xml version="1.0" encoding="UTF-8"?>
<CmConfig xmlns="http://purl.org/cloudmeter/config" version="6.1.0">
  <Port>8889</Port>
  <UIDirectory>../ui</UIDirectory>
  <DataDirectory>../data</DataDirectory>
  <LogConfig>streamfwdlog.conf</LogConfig>
  <Capture>
    <InterfaceRegex>(en|eth|lo)[0-9]*</InterfaceRegex>
    <Offline>false</Offline>
  </Capture>
</CmConfig>

2) To ensure that the wire input is enabled, place this file in local/inputs.conf 

[streamfwd://streamfwd]
splunk_stream_app_location = http://localhost:8000/en-us/custom/splunk_app_stream/
disabled = 1

Then restart your Splunk instance.

3) Now ensure that you are collecting "response_time" and "src_headers" fields under the http configuration.

Now, all of the dashboards should have data after you log into your Splunk instance.


### System Performance 

This requires updates to the Splunk_TA_nix:

1) For Yosemite users, update line 45 in top.sh:
vi +45 /opt/splunk/etc/apps/Splunk_TA_nix/bin/top.sh
Replace rshrd with vprvt
This may not be a proper replacement, but it fixes it enough to get data in this dashboard.


### Clicks!:

This dashboard is fueled by the clickcounter.py script in the bin dir.  There are a couple of things you need 
to do to enure everything works as expected.  I plan on automating more of these functions as soon as I can 
figure it out.

1) The monitor stanza assumes that you are using the same default sirectory that I am:

	/opt/splunk/etc/apps/stream_splunk_usage_demo/data/output.log

2) The script needs to be launched manually to start tracking clicks.  It takes about 5 seconds to begin recording.

	/opt/splunk/etc/apps/stream_splunk_usage_demo/bin/clickcounter.py

I want to add tracking of keyboard clicks, window resizing, and trackpad distance travel...





