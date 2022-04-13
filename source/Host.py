#!/usr/bin/env python3

import random

class Host:
		
	def __init__(self, policy, hostId):
		self.policy = policy
		self.key = self.__setKey()
		self.hostId = hostId
		
	#Generates random key for this host
	def __setKey(self):
		key = random.randint(1000,9999)
		return key
		
	#Returns the key of this host
	def getKey(self):
		return self.key
		
	#Returns the host ID of this host
	def getHostId(self):
		return self.hostId
		
	#Returns the policy from this host
	def getPolicy(self):
		return self.policy
		
	#Set the host policy, takes policy object
	def setPolicy(self, policy):
		self.policy = policy
	
	#Describe the object
	def toString(self):
		info = "Host ID: " + str(self.getHostId()) + "\nHost Key: " + str(self.getKey())
		return info
		
		

		
		


	
