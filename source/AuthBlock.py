#!/usr/bin/env python3

from source.AuthNode import AuthNode
from source.Host import Host
import hashlib
import time

class AuthBlock:

	def __init__(self, host: Host):
		self.head = AuthNode(host)
		
	def add_node(self, host: Host):
		new_node = AuthNode(host)
		last_node = self.get_last_node()
		last_node.set_next(new_node)
		last_node.set_hash(self.__calc_hash(last_node.get_key(), new_node.get_key()))
			
	def get_last_node(self) -> AuthNode:
		cur_node = self.head
		while(cur_node.get_next() != None):
			cur_node = cur_node.get_next()
		return cur_node
		
	def __calc_hash(self, last_key, new_key) -> str:
		encode_last = str(last_key).encode()
		last_hash = hashlib.sha256(encode_last).hexdigest()
		concat = last_hash + str(new_key)
		encode_concat = concat.encode()
		full_hash = hashlib.sha256(encode_concat).hexdigest()
		return full_hash
		
	def print_chain(self):
		cur_node = self.head
		print("\n-----PRINTING-----\n")
		while(cur_node != None):
			print(cur_node.to_string())
			cur_node = cur_node.get_next()
		
	def validate(self, host) -> bool:
		key = host.get_key()
		host_id = host.get_host_id()
		valid = False
		cur_node = self.head
		while(cur_node != None):
			cur_key = cur_node.get_key()
			cur_id = cur_node.get_id()
			if(cur_key == key and cur_id == host_id):
				valid = True
			cur_node = cur_node.get_next()
		return valid
	
	
	#Hash key of prev, concat to current key, hash concatentaion, set as hash of previous
