from source.NetworkDecentralized import Network
from source.Policy import Policy
from source.Host import Host

class NetworkTestCases:

    def test_success_same_policy(self):
        pol1 = Policy("1:00", "23:59")
        h1 = Host(pol1, 'h1')
        h2 = Host(pol1, 'h2')
        net = Network(hosts=[h2, h1])
        print('h2 initiates communication with h1...')
        print('performing block chain validation...')
        result = net.block_auth_host(net.get_host_by_id('h2'))
        print(f'is h2 valid? {result}')
        result = net.get_host_by_id('h1').get_policy().policy_validation(net.get_host_by_id('h2'))
        print(f'do h1 and h2 have the same policy? {result}')
        result = net.validate_hosts_policy(net.get_host_by_id('h1'), net.get_host_by_id('h2'))
        print(f'are h1 and h2 authorized? {result}')

    def test_success_policy_sync(self):
        pol1 = Policy("1:00", "23:59")
        pol_diff = Policy("12:32", "16:00")
        hosts = []
        for x in range(1, 10):
            hosts.append(Host(pol1, f"h{str(x)}"))
        hosts.append(Host(pol_diff, "h10"))
        net = Network(hosts=hosts)
        print('h10 initiates communication with h5...')
        print('performing block chain validation...')
        result = net.block_auth_host(net.get_host_by_id('h10'))
        print(f'is h10 valid? {result}')
        result = net.get_host_by_id('h5').get_policy().policy_validation(net.get_host_by_id('h10'))
        print(f'do h10 and h5 have the same policy? {result}')
        print('attempting to sync policies..')
        result = net.validate_hosts_policy(net.get_host_by_id('h5'), net.get_host_by_id('h10'))
        print(f'are h10 and h5 authorized? {result}')

    def test_failure_host_key_not_authorized(self):
        pol1 = Policy("1:00", "23:59")
        hosts = []
        for x in range(1, 10):
            hosts.append(Host(pol1, f"h{str(x)}"))
        net = Network(hosts=hosts)
        unauth_host = (Host(pol1, "h10"))
        print('h10 initiates communication with h3...')
        print('performing block chain validation...')
        result = net.block_auth_host(unauth_host)
        print(f'is h10 valid? {result}')
    
    def test_failure_unauthorized_policy_criteria(self):
        pol1 = Policy("23:58", "23:59")
        h1 = Host(pol1, 'h1')
        h2 = Host(pol1, 'h2')
        net = Network(hosts=[h2, h1])
        print('h2 initiates communication with h1...')
        print('performing block chain validation...')
        result = net.block_auth_host(net.get_host_by_id('h2'))
        print(f'is h2 valid? {result}')
        result = net.get_host_by_id('h1').get_policy().policy_validation(net.get_host_by_id('h2'))
        print(f'do h1 and h2 have the same policy? {result}')
        result = net.validate_hosts_policy(net.get_host_by_id('h1'), net.get_host_by_id('h2'))
        print(f'are h1 and h2 authorized? {result}')

