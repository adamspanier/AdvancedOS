#!/usr/bin/env python3

from source.Policy import Policy
from source.Host import Host
from source.AuthNode import AuthNode
from source.AuthBlock import AuthBlock

def main():
	#Policy Tests
	#To make a policy, choose a begin time and end time to choose window of allowable access
	new_pol = Policy("12:00", "15:00")
	new_pol2 = Policy("13:00", "15:00")
	print(new_pol.get_hash())
	print(new_pol2.get_hash())
	
	#Host Tests
	#To make a host, give it a policy and an ID in the form of a String
	new_host = Host(new_pol, "h1")
	print(new_host.to_string())
	print(new_host.get_policy().get_hash())
	
	#AuthNode Tests
	new_node = AuthNode(new_host)
	print(new_node.get_key())
	print(new_node.get_id())
	
	#Blockchain Tests
	#To make a new auth blockchain, give it a head.
	new_block = AuthBlock(new_host)
	print(new_block.head.get_id())
	new_host2 = Host(new_pol, "h2")
	new_host3 = Host(new_pol, "h3")
	new_host4 = Host(new_pol, "h4")
	new_host5 = Host(new_pol, "h5")
	new_host6 = Host(new_pol2, "h6")
	
	#To add hosts to the auth blockchain, use the add_node() function
	new_block.add_node(new_host2)
	new_block.add_node(new_host3)
	new_block.add_node(new_host4)
	new_block.print_chain()
	
	#To check if a host is in the blockchain, call the blockchain.validate() function with a host
	print("Is H2 valid? " + str(new_block.validate(new_host2)))
	print("Is H5 valid? " + str(new_block.validate(new_host5)))
	
	#Interhost Policy validation
	#To check if h1 and h2 have same policy, use h1.get_policy().policy_validation(h2)
	print("Do h1 and h2 have the same policy? " + str(new_host.get_policy().policy_validation(new_host2)))
	print("Do h1 and h6 have the same policy? " + str(new_host.get_policy().policy_validation(new_host6)))
	
	#To check the policy rules, use h1.get_policy().check_auth(), no args
	print("Can I login now? " + str(new_host.get_policy().check_auth()))

if __name__ == "__main__":
	main()
