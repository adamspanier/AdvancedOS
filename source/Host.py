#!/usr/bin/env python3

import random
from source.Policy import Policy

class Host:
		
	def __init__(self, policy: Policy, host_id: str):
		self.policy = policy
		self.key = self.__set_key()
		self.host_id = host_id
		
	#Generates random key for this host
	def __set_key(self) -> int:
		key = random.randint(1000,9999)
		return key
		
	#Returns the key of this host
	def get_key(self) -> int:	
		return self.key
		
	#Returns the host ID of this host
	def get_host_id(self) -> str:
		return self.host_id
		
	#Returns the policy from this host
	def get_policy(self) -> Policy:
		return self.policy
		
	#Set the host policy, takes policy object
	def set_policy(self, policy):
		self.policy = policy
	
	#Describe the object
	def to_string(self) -> str:
		info = "Host ID: " + str(self.get_host_id()) + "\nHost Key: " + str(self.get_key())
		return info
		
		

		
		


	
