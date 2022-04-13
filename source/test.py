#!/usr/bin/env python3

from Policy import Policy
from Host import Host
from AuthNode import AuthNode
from AuthBlock import AuthBlock

def main():
	#Policy Tests
	#To make a policy, choose a begin time and end time to choose window of allowable access
	newPol = Policy("12:00", "15:00")
	newPol2 = Policy("13:00", "15:00")
	print(newPol.getHash())
	print(newPol2.getHash())
	
	#Host Tests
	#To make a host, give it a policy and an ID in the form of a String
	newHost = Host(newPol, "h1")
	print(newHost.toString())
	print(newHost.getPolicy().getHash())
	
	#AuthNode Tests
	newNode = AuthNode(newHost)
	print(newNode.getKey())
	print(newNode.getId())
	
	#Blockchain Tests
	#To make a new auth blockchain, give it a head.
	newBlock = AuthBlock(newHost)
	print(newBlock.head.getId())
	newHost2 = Host(newPol, "h2")
	newHost3 = Host(newPol, "h3")
	newHost4 = Host(newPol, "h4")
	newHost5 = Host(newPol, "h5")
	newHost6 = Host(newPol2, "h6")
	
	#To add hosts to the auth blockchain, use the addNode() function
	newBlock.addNode(newHost2)
	newBlock.addNode(newHost3)
	newBlock.addNode(newHost4)
	newBlock.printChain()
	
	#To check if a host is in the blockchain, call the blockchain.validate() function with a host
	print("Is H2 valid? " + str(newBlock.validate(newHost2)))
	print("Is H5 valid? " + str(newBlock.validate(newHost5)))
	
	#Interhost Policy validation
	#To check if h1 and h2 have same policy, use h1.getPolicy().policyValidation(h2)
	print("Do h1 and h2 have the same policy? " + str(newHost.getPolicy().policyValidation(newHost2)))
	print("Do h1 and h6 have the same policy? " + str(newHost.getPolicy().policyValidation(newHost6)))
	
	#To check the policy rules, use h1.getPolicy().checkAuth(), no args
	print("Can I login now? " + str(newHost.getPolicy().checkAuth()))

if __name__ == "__main__":
	main()
