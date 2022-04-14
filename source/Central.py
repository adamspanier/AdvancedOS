import time
from source.AuthBlock import AuthBlock
from source.Host import Host
from source.Policy import Policy
import matplotlib.pyplot as plt
import numpy as np


def main():
    # Creating a central policy engine
    central_policy = Policy("12:00", "15:00")
    central_host = Host(central_policy, "central")
    central_block = AuthBlock(central_host)

    # Creating random hosts
    host_policy = Policy("12:00", "15:00")
    hosts = []

    # Generating multiple requests and calculating the total time
    central_times = []
    for t in range(1, 20):

        for i in range(t):
            new_host = Host(host_policy, f'h{i}')
            hosts.append(new_host)
            central_block.addNode(new_host)
            print(f'h{i} added to the block chain')

        start_time = time.time()

        for i in range(t):
            print(f'Validating h{i}; result: {central_block.validate(hosts[i])}')

        central_times.append(time.time() - start_time)

    # Simulating distributed system where each host validates single time
    dist_time = []
    for t in range(1, 20):
        start_time = time.time()
        new_host = Host(host_policy, f'h{t}')
        print(f'h{t} added to the block chain')
        print(f'Validating h{t}; result: {central_block.validate(new_host)}')
        dist_time.append(time.time() - start_time)

    # Plotting the graph for comparison
    plt.plot(np.arange(1, 20, dtype=int), np.array(central_times))
    plt.plot(np.arange(1, 20, dtype=int), np.array(dist_time))
    plt.legend(['Centralized', 'Distributed'])
    plt.xlabel('No. of hosts')
    plt.ylabel('Time (s)')
    plt.title('Centralized vs. distributed zero trust architecture')
    plt.show()


if __name__ == '__main__':
    main()
