from AppKit import NSWorkspace
from time import sleep
from Quartz import *
import csv
 
counter = 0
 
def printdata(a,b):
  global counter 
  activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
  print activeAppName 
  print counter
	
  with open('../data/output.csv','a') as outfile:
	writer = csv.writer(outfile)
	'app='+outfile.write(str(activeAppName)+' clickcount='+str(counter)+'\n')
	counter = 0 
	
def MyFunction(p, t, e, c):
	global counter
	counter = counter + 1
	print e
 
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
