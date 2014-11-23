Author:  James Donn

This demo requires a few configuration updates in other Apps to work.  This doc breaks down what each dashboard requires.

Stream Splunk HTTP and User Access Data Dashboard:

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


System Performance Dashboard:

This requires updates to the Splunk_TA_nix:

1) For Yosemite users, update line 45 in top.sh:
vi +45 /opt/splunk/etc/apps/Splunk_TA_nix/bin/top.sh
Replace rshrd with vprvt
This may not be a proper replacement, but it fixes it enough to get data in this dashboard.







