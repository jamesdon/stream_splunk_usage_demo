#!/usr/bin/python
from AppKit import NSWorkspace
from time import sleep
from Quartz import *
import time

### Set the counter
counter = 0
 
def printdata(a,b):
  global counter 
  activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
  f = open('../data/output.log','a')
  f.write(time.asctime(time.localtime(time.time())) + ' app="' + str(activeAppName) + '" cps=' + str(counter)+'\n')
  counter = 0 
	
def MyFunction(p, t, e, c):
	global counter
	counter = counter + 1
 
tap = CGEventTapCreate(kCGHIDEventTap, kCGHeadInsertEventTap,
    kCGEventTapOptionListenOnly, CGEventMaskBit(kCGEventLeftMouseDown),
    MyFunction, None)
 
runLoopSource = CFMachPortCreateRunLoopSource(None, tap, 0);
CFRunLoopAddSource(CFRunLoopGetCurrent(), runLoopSource, kCFRunLoopDefaultMode);
 
timer = CFRunLoopTimerCreate (
    kCFAllocatorDefault,
   CFAbsoluteTimeGetCurrent(),
   1,
   0,
   0,
   printdata,
   None)
 
CFRunLoopAddTimer(CFRunLoopGetCurrent(),timer, kCFRunLoopCommonModes)
 
CGEventTapEnable(tap, True);
 
CFRunLoopRun();
