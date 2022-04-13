#!/usr/bin/env python3

from AuthNode import AuthNode
import hashlib
import time

class AuthBlock:

	def __init__(self, host):
		self.head = AuthNode(host)
		
	def addNode(self, host):
		newNode = AuthNode(host)
		lastNode = self.getLastNode()
		lastNode.setNext(newNode)
		lastNode.setHash(self.__calcHash(lastNode.getKey(), newNode.getKey()))
			
	def getLastNode(self):
		curNode = self.head
		while(curNode.getNext() != None):
			curNode = curNode.getNext()
		return curNode
		
	def __calcHash(self, lastKey, newKey):
		encodeLast = str(lastKey).encode()
		lastHash = hashlib.sha256(encodeLast).hexdigest()
		concat = lastHash + str(newKey)
		encodeConcat = concat.encode()
		fullHash = hashlib.sha256(encodeConcat).hexdigest()
		return fullHash
		
	def printChain(self):
		curNode = self.head
		print("\n-----PRINTING-----\n")
		while(curNode.getNext() != None):
			print(curNode.toString())
			curNode = curNode.getNext()
		print(curNode.toString())
		
	def validate(self, host):
		key = host.getKey()
		hostId = host.getHostId()
		valid = False
		curNode = self.head
		while(curNode.getNext() != None):
			curKey = curNode.getKey()
			curId = curNode.getId()
			if(curKey == key and curId == hostId):
				valid = True
			curNode = curNode.getNext()
		return valid
	
	
	#Hash key of prev, concat to current key, hash concatentaion, set as hash of previous
