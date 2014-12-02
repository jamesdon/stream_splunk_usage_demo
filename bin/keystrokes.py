#!/usr/bin/env python
# cocoa_keypress_monitor.py by Bjarte Johansen is licensed under a
# License: http://ljos.mit-license.org/
 
from AppKit import NSApplication, NSApp
from Foundation import NSObject, NSLog
from Cocoa import (NSEvent, NSKeyDownMask, NSCommandKeyMask, NSControlKeyMask, NSAlternateKeyMask, NSShiftKeyMask, NSLeftMouseDownMask, NSRightMouseDownMask, NSMouseMovedMask, NSScrollWheelMask, NSFlagsChangedMask)
from PyObjCTools import AppHelper
import logging
 
class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
	mask = (NSKeyDownMask
		| NSCommandKeyMask
		| NSControlKeyMask
		| NSAlternateKeyMask
		| NSShiftKeyMask
		| NSLeftMouseDownMask
		| NSRightMouseDownMask
		| NSMouseMovedMask
		| NSScrollWheelMask
		| NSFlagsChangedMask)
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)
 
def handler(event):
    try:
        # logging.info(str(event))
        logging.info(str(event).replace('\r', ' <RETURN>').replace('\n', ' <NEWLINE>').replace('\t', ' <TAB>').replace('\" \"', '\" <SPACE>\"'))
    except UnicodeEncodeError as e:
	# logging.info(event.encode('ascii', 'xmlcharrefreplace'))
        logging.info(event)
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()
    except Exception as e:
        logging.info(e)
 
def main():
    app = NSApplication.sharedApplication()
    logging.basicConfig(filename='../data/jim.log', format='%(asctime)s %(message)s', level=logging.INFO)
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()
 
if __name__ == '__main__':
    main()
