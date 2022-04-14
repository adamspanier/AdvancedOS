#!/usr/bin/env python3


#Auth Node Object
#	1. this.next() -> hashPointer - head is null, traverse starting at tail. Contains the hash of current key plus the hash of previous key. h(n-1)
#	2. this.key - arbitrary key value, 4 digit int.
#	3. this.host_id() - spits out h1, h2, h3

class AuthNode:
		
	#Next is null for head
	def __init__(self, host):
		self.next_node = None
		self.key = host.get_key()
		self.host_id = host.get_host_id()
		self.prev_hash = None
		
	def get_next(self):
		return self.next_node

	def set_next(self, in_node):	
		self.next_node = in_node
		
	def get_key(self):
		return self.key
		
	def get_id(self):
		return self.host_id
		
	def set_hash(self, in_hah):	
		self.prev_hash = in_hah
		
	def get_hash(self):
		return self.prev_hash
		
	def to_string(self):
		info = "Host ID: " + str(self.get_id()) + "\nHost Key: " + str(self.get_key()) + "\nHash: " + str(self.get_hash())
		return info
		
		
		
		
		

		
		


	
