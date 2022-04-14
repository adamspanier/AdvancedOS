from source.Host import Host
from source.AuthBlock import AuthBlock
from typing import Union

class Network:

    def __init__(self, host: Host = None, hosts: list[Host] = None):
        if host == None and hosts == None:
            raise KeyError("must provide a host or list of hosts")
        if host and hosts:
            raise KeyError("can only provide one value, not both")
        if host:
            self.hosts = [host]
            self.policies = [host.get_policy()]
            self.authentication_blockchain = AuthBlock(host)
        if hosts:
            first_host = hosts.pop()
            self.hosts = [first_host]
            self.policies = [first_host.get_policy()]
            self.authentication_blockchain = AuthBlock(first_host)
            self.add_hosts(hosts)

    
    def add_host(self, host: Host):
        self.hosts.append(host)
        self.policies.append(host.get_policy())
        self.authentication_blockchain.add_node(host)
    
    def add_hosts(self, hosts: [Host]):
        for host in hosts:
            self.add_host(host)
    
    def get_host_by_id(self, id: str):
        for host in self.hosts:
            if host.get_host_id() == id:
                return host
    
    def block_auth_host(self, new_host: Host):
        return self.authentication_blockchain.validate(new_host)
    
    def validate_hosts_policy(self, validator: Host, other_host: Host):
        validator_policy = validator.get_policy()
        if validator_policy.policy_validation(other_host):
            return validator_policy.check_auth()

        most_occuring_policy = max(set(self.policies), key = self.policies.count)
        print("synchronizing policies..")
        for host in self.hosts:
            host.set_policy(most_occuring_policy)
        
        res = validator.get_policy().policy_validation(other_host)
        print(f"do {validator.get_host_id()} and {other_host.get_host_id()} have the same policy? {res}")
        return validator_policy.check_auth()
        
        
