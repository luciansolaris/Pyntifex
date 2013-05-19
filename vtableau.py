#!/usr/bin/python2.7 -tt

#Imports:
import sys

class Vtableau(object):
 __inString = r''
 __outString = r''
 __key = r''
 __alphabet = r''

 def __init__(self, inStr=r'', inKey=r'', inAlpha=r''):
  if len(inStr)==len(inKey) and len(inStr)>0 and len(inAlpha)>0:
   for ii in inStr:
    if ii not in inAlpha:
     print '\n(EE): Invalid character not in alphabet found in input:','\''+ii+'\''
     print commandString()
     raise Exception('(EE): Invalid character not in alphabet found in input:','\''+ii+'\'')
   self.__inString = inStr
   for ii in inKey:
    if ii not in inAlpha:
     print '\n(EE): Invalid character not in alphabet found in inputted key:','\''+ii+'\''
     print commandString()
     raise Exception('(EE): Invalid character not in alphabet found in inputted key:','\''+ii+'\'')
   self.__key = inKey
   self.__alphabet = inAlpha
  elif len(inStr)>len(inKey):
   print '\n(EE): Message length is longer than key length'
   print commandString()
   raise Exception('(EE): Message length is longer than key length')
  elif len(inStr)<len(inKey):
   print '\n(EE): Message length is shorter than key length'
   print commandString()
   raise Exception('(EE): Message length is shorter than key length')
  elif len(inStr)<=0 or len(inKey)<=0 or len(inAlpha)<=0:
   print '\n(EE): One or more inputs empty'
   print commandString()
   raise Exception('(EE): One or more inputs empty')
  else:
   print '\n(EE): Unknown Error in Vtableau constructor'
   print commandString()
   raise Exception('(EE): Unknown Error in Vtableau constructor, this line should never have been reached')

 def returnEnciphered(self):
  for ii in range(len(self.__inString)):
#   print __alphabet[(__alphabet.index(__inString[ii])+__alphabet.index(__key[ii]))%len(__alphabet)]+'.'
   self.__outString=self.__outString+self.__alphabet[(self.__alphabet.index(self.__inString[ii])+self.__alphabet.index(self.__key[ii]))%len(self.__alphabet)]
  return self.__outString

 def returnDeciphered(self):
  for ii in range(len(self.__inString)):
   self.__outString=self.__outString+self.__alphabet[(len(self.__alphabet)+self.__alphabet.index(self.__inString[ii])-self.__alphabet.index(self.__key[ii]))%len(self.__alphabet)]
  return self.__outString


#Main Function:
def main():
 try:
  inOpts=checkOptions()
 except:
  print '\n(EE): Input options malformed, check execution options'
  print commandString()
  sys.exit(1)
 if '--debug' in sys.argv:
  debugScript()
  sys.exit(0)
 elif '--help' in sys.argv:
  printHelp()
  sys.exit(0)
 elif (0 not in inOpts[:2]) and (inOpts[2]==1 or inOpts[2]==2):
  if inOpts[2]==1:
   print Vtableau(sys.argv[sys.argv.index('-e')+1], sys.argv[sys.argv.index('-k')+1], sys.argv[sys.argv.index('-a')+1]).returnEnciphered()
  elif inOpts[2]==2:
   print Vtableau(sys.argv[sys.argv.index('-d')+1], sys.argv[sys.argv.index('-k')+1], sys.argv[sys.argv.index('-a')+1]).returnDeciphered()
  else:
   print '\n(EE): Options Processing Error, check main() code'
   print commandString()
   sys.exit(1)
 else:
  print '\n(EE): Options provided insufficient or are unhandled'
  print commandString()
  sys.exit(1)
 sys.exit

def checkOptions():
 inOpts=[0,0,0]
 if ('-e' in sys.argv) and ('-d' not in sys.argv) and (sys.argv[sys.argv.index('-e')+1][0] is not '-'):
  inOpts[2]=1
 if ('-d' in sys.argv) and ('-e' not in sys.argv) and (sys.argv[sys.argv.index('-d')+1][0] is not '-'):
  inOpts[2]=2
 if '-a' in sys.argv and (sys.argv[sys.argv.index('-a')+1][0] is not '-'):
  inOpts[1]=1
 if '-k' in sys.argv and (sys.argv[sys.argv.index('-k')+1][0] is not '-'):
  inOpts[0]=1
 return inOpts

def debugScript():
 inString2 = r'testmessage'
 outString2 = r''
 key2 = r'mnopqrstuvx'
 alphabet2 = r'abcdefghijklmnopqrstuvwxyz'

 tableau1 = Vtableau(inString2, key2, alphabet2)

 print '\ninput:',inString2
 print 'key:',key2
 print 'alphabet:',alphabet2
 tempString=tableau1.returnEnciphered()[:]
 print 'output:',tempString

 tableau2 = Vtableau(tempString, key2, alphabet2)

 print '\ninput:',tempString
 print 'key:',key2
 print 'alphabet:',alphabet2
 tempString2=tableau2.returnDeciphered()[:]
 print 'output:',tempString2

 print commandString()

 sys.exit(0)

def printHelp():
 print 'Command line options:'
 print ' -e <String> | Encipher String'
 print ' -d <String> | Decipher String'
 print ' -a <String> | Cipher Alphabet'
 print ' -k <String> | Cipher Key'
 print '\nThis Python Script provides OTP tableau functionality'
 print 'via the command line or by importing this module and'
 print 'creating an instance of Vtableau(input, key, alphabet),'
 print 'then calling .returnEnciphered() or .returnDeciphered()'

def commandString():
 outStr='\nAs executed: '
 for ii in sys.argv:
  outStr=outStr+str(ii)+' '
 return outStr

#Boilerplate:
if __name__=='__main__':
 main()
