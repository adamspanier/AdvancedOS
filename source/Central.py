import time
from source.AuthBlock import AuthBlock
from source.Host import Host
from source.Policy import Policy
import matplotlib.pyplot as plt
import numpy as np


def main():
    central_policy = Policy("12:00", "15:00")
    central_host = Host(central_policy, "central")

    central_block = AuthBlock(central_host)

    host_policy = Policy("12:00", "15:00")
    hosts = []

    times = []

    for t in range(5, 20):

        for i in range(t):
            new_host = Host(host_policy, f'h{i}')
            hosts.append(new_host)
            central_block.addNode(new_host)
            print(f'h{i} added to the block chain')

        start_time = time.time()

        for i in range(t):
            print(f'Validating h{i}; result: {central_block.validate(hosts[i])}')

        times.append(time.time() - start_time)

    print(len(times))

    plt.plot(np.arange(5, 20), np.array(times))
    plt.show()


if __name__ == '__main__':
    main()
