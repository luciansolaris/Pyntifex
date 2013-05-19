#!/usr/bin/python2.7

import os
import struct
import sys

randomDevice=open('/dev/random','rb')
urandomDevice=open('/dev/urandom','rb')
UINT32_MAX=0xffffffff

def randomDeviceBytes(inLength):
 return randomDevice.read(inLength)

def urandomDeviceBytes(inLength):
 return urandomDevice.read(inLength)

def convertBytesToInt(inBytes):
 return struct.unpack('I',inBytes)[0]

def makeAcceptableInt(inLower, inUpper, inInt):
 if inLower>=0 and inUpper>inLower and inInt>=0:
  return int((((inUpper-inLower)/float(UINT32_MAX))+inLower)*inInt)

def randomGet(inLower, inUpper, inCount):
 if inLower>=0 and inUpper>inLower and inCount>0:
  return [makeAcceptableInt(inLower, inUpper, convertBytesToInt(randomDeviceBytes(4))) for _ in range(inCount)]
 else:
  raise Exception('(EE): Bad arguments for randomGet()')

def urandomGet(inLower, inUpper, inCount):
 if inLower>=0 and inUpper>inLower and inCount>0:
  return [makeAcceptableInt(inLower, inUpper, convertBytesToInt(urandomDeviceBytes(4))) for _ in range(inCount)]
 else:
  raise Exception('(EE): Bad arguments for urandomGet()')

def main():
 args=[None]
 if len(sys.argv)==4 and long(sys.argv[1])<long(sys.argv[2]) and long(sys.argv[3])>=0:
  for i in sys.argv[1:]:
   args.append(int(i))
  print '\nurandom Output:'
  for i in urandomGet(args[1],args[2],args[3]):
   print i,
  print '\n\nrandom Output:'
  for i in randomGet(args[1],args[2],args[3]):
   print i,
  print '\n\nDebug Check Complete...'
 else:
  print '(EE): Error in arguments.  Usage: ./command Lower Upper Count'


if __name__=='__main__':
 main()
