#!/usr/bin/env python3

import hashlib
import time
import datetime

class Policy:
		
	def __init__(self, begin, end):
		self.begin = begin
		self.end = end
		
	#Convert string time to datetime
	def convert(self, begin, end, cur):
		beginSplit = begin.split(':')
		endSplit = end.split(':')
		curSplit = cur.split(':')
		newBegin = datetime.time(int(beginSplit[0]), int(beginSplit[1]))
		newEnd = datetime.time(int(endSplit[0]), int(endSplit[1]))
		newCur = datetime.time(int(curSplit[0]), int(curSplit[1]), int(curSplit[2]))
		return newBegin, newEnd, newCur
		
	#Private function to convert policy to hash
	def __toHash(self):
		value = self.toString()
		encoded = value.encode()
		result = hashlib.sha256(encoded).hexdigest()
		return result
		
	#Retrieve the hash of this policy
	def getHash(self):
		return self.__toHash()
		
	#Checks to see if login is in approprate time frame
	def checkAuth(self):
		now = time.strftime("%H:%M:%S")
		print(now)
		newBegin, newEnd, newCur = self.convert(self.begin, self.end, now)
		valid = False
		
		if(newCur > newBegin and newCur < newEnd):
			valid = True
			
		return valid
		
	#Takes in a policy object
	def policyValidation(self, h2):
		valid = False
		if(self.getHash() == h2.getHash()):
			valid = True
		return valid
		
	#Describe this policy
	def toString(self):
		info = "The begin time is " + str(self.begin) + " and the end time is " + str(self.end) + "."
		return info
		
		


	
