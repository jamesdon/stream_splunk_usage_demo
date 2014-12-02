#!/usr/bin/env python
# cocoa_keypress_monitor.py by Bjarte Johansen is licensed under a
# License: http://ljos.mit-license.org/
 
from AppKit import NSApplication, NSApp
from Foundation import NSObject, NSLog
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper
import logging
 
class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        mask = NSKeyDownMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)
 
def handler(event):
    try:
        #NSLog(u"%@", event)
        logging.info(event)
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()
 
def main():
    app = NSApplication.sharedApplication()
    #logging.basicConfig(filename='../data/keys.log', format='%(asctime)s %(message)s %(app)s', level=logging.INFO)
    logging.basicConfig(filename='../data/keys.log', format='%(asctime)s %(message)s', level=logging.INFO)
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()
 
if __name__ == '__main__':
    main()
