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
		begin_split = begin.split(':')
		end_split = end.split(':')
		cur_split = cur.split(':')
		new_begin = datetime.time(int(begin_split[0]), int(begin_split[1]))
		new_end = datetime.time(int(end_split[0]), int(end_split[1]))
		new_cur = datetime.time(int(cur_split[0]), int(cur_split[1]), int(cur_split[2]))
		return new_begin, new_end, new_cur
		
	#Private function to convert policy to hash
	def __to_hash(self) -> str:
		value = self.to_string()
		encoded = value.encode()
		result = hashlib.sha256(encoded).hexdigest()
		return result
		
	#Retrieve the hash of this policy
	def get_hash(self) -> hash:
		return self.__to_hash()
		
	#Checks to see if login is in approprate time frame
	def check_auth(self) -> bool:
		now = time.strftime("%H:%M:%S")
		#print(now)
		new_begin, new_end, new_cur = self.convert(self.begin, self.end, now)
		valid = False
		
		if(new_cur > new_begin and new_cur < new_end):
			valid = True
			
		return valid
		
	#Takes in a policy object
	def policy_validation(self, h2) -> bool:
		valid = False
		if(self.get_hash() == h2.get_policy().get_hash()):
			valid = True
		return valid
		
	#Describe this policy
	def to_string(self) -> str:
		info = "The begin time is " + str(self.begin) + " and the end time is " + str(self.end) + "."
		return info

	def getPolicy(self):
		pass
		
		


	
