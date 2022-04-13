#!/usr/bin/env python3


#Auth Node Object
#	1. this.next() -> hashPointer - head is null, traverse starting at tail. Contains the hash of current key plus the hash of previous key. h(n-1)
#	2. this.key - arbitrary key value, 4 digit int.
#	3. this.hostId() - spits out h1, h2, h3

class AuthNode:
		
	#Next is null for head
	def __init__(self, host):
		self.nextNode = None
		self.key = host.getKey()
		self.hostId = host.getHostId()
		self.prevHash = None
		
	def getNext(self):
		return self.nextNode

	def setNext(self, inNode):	
		self.nextNode = inNode
		
	def getKey(self):
		return self.key
		
	def getId(self):
		return self.hostId
		
	def setHash(self, inHash):	
		self.prevHash = inHash
		
	def getHash(self):
		return self.prevHash
		
	def toString(self):
		info = "Host ID: " + str(self.getId()) + "\nHost Key: " + str(self.getKey()) + "\nHash: " + str(self.getHash())
		return info
		
		
		
		
		

		
		


	
