#!/usr/bin/python2.7
'''Module password makes passwords according to criteria passed to the constructor of the PasswordMaker() class.  This module employs Vtableau, Deck, and Formatter to operate.  It creates 3 Deck()s of randomly ordered alphabets and runs their outputs through a Vtableau() doEnc/doDec combo, combining them at the end and passing them though Formatter()'s format().  The Deck()s are nested decks, meaning that the makeDeck function makes a deck using the alphabet, randomizes it, then puts the deck into a bigger deck of decks, repeat.  This is done to attempt to correct the letter bias in standard Pontifex.  This module was meant to be run from the command line.'''

import sys
import os
import re
import solitaire
import vtableau
import formatter

class PasswordMaker(object):
 '''Class PasswordMaker makes passwords and prints them.'''
 def __init__(self, inAlpha, charsPerGroup=8, groupsPerLine=6):
  '''Constructor is to be called with the following options:
  (rawstr)inAlpha - Alphabet name (from solitaire module alphaDict) to derive password(s) from.
  (int)charsPerGroup - [Optional] Number of characters per group (Default 8).
  (int)groupsPerLine - [Optional] Number of groups per line (Default 6).'''
  self.__alpha=solitaire.alphaDict.get(inAlpha)
  self.__deck1=self.makeDeck(self.__alpha)
  self.__deck2=self.makeDeck(self.__alpha)
  self.__deck3=self.makeDeck(self.__alpha)
  self.__vtableau=vtableau.Vtableau(self.__alpha,self.__alpha[0],self.__alpha[0])
  self.__formatter=formatter.Formatter(charsPerGroup,groupsPerLine," ")

 def makeDeck(self, inAlpha):
  '''Makes a nested deck of decks, each internal deck containing the letters of inAlpha.  There are len(inAlpha) inner decks in the container deck.  Returns the outer deck.'''
  deck=solitaire.Deck()
  for i in xrange(len(inAlpha)):
   deck2=solitaire.Deck()
   deck2.makeDeck(inAlpha,10)
   deck2.lockDeck()
   deck.pushAlpha(deck2)
  deck.pushJoker(1)
  deck.pushJoker(2)
  deck.shuffleVal(100)
  deck.shuffleDeck(10)
  deck.lockDeck()
  return deck

 def getNextChar(self):
  '''Returns the next character in the password making process'''
  return self.__vtableau.doDec(self.__vtableau.doEnc(self.__deck1.getObj().getKey(1),self.__deck2.getObj().getKey(1)),self.__deck3.getObj().getKey(1))

 def makePassword(self, inLength):
  '''Makes and returns a password string that is to be formatted into groups.'''
  returnString=""
  for i in xrange(inLength):
   returnString=returnString+str(self.getNextChar())
  return returnString

 def printPassword(self, passwordString):
  '''Takes a long password string and cuts it into groups.'''
  print self.__formatter.format(passwordString)

def main():
 if '--help' in sys.argv:
  print "Usage: ./command AlphabetName CharsPerGroup GroupsPerLine Lines"
  sys.exit(0)
 groupLength=int(sys.argv[2])
 numGroups=int(sys.argv[3])
 numPasswords=int(sys.argv[4])
 maker1=PasswordMaker(sys.argv[1],groupLength,numGroups)
 maker1.printPassword(maker1.makePassword(groupLength*numGroups*numPasswords))
 sys.exit(0)

if __name__=='__main__':
 main()
