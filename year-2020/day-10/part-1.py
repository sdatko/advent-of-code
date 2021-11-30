#!/usr/bin/env python3
#
# Task:
# You have a bag of power adapters (with the unit of joltage).
# Each of your joltage adapters is rated for a specific output joltage
# (your puzzle input). Any given adapter can take an input 1, 2, or 3 jolts
# lower than its rating and still produce its rated output joltage.
# In addition, your device has a built-in joltage adapter rated for 3 jolts
# higher than the highest-rated adapter in your bag.
# Treat the charging outlet near your seat as having an effective joltage
# rating of 0.
# Find a chain that uses all of your adapters to connect the charging outlet
# to your device's built-in adapter and count the joltage differences between
# the charging outlet, the adapters, and your device. What is the number of
# 1-jolt differences multiplied by the number of 3-jolt differences?
#
# Solution:
# What we need to do, is basically read the input file as list of adapters,
# append the joltage value for wall socket (zero) and for the device we want
# to power up. Then we just need to sort this list and calculate differences
# between each next two elements. Finally we count how many differences of
# 1 and 3 are there and multiply these counts.
#

INPUT_FILE = 'input.txt'

SOCKET_VALUE = 3


def main():
    numbers = sorted(
        [int(number)
            for number in open(INPUT_FILE, 'r').read().strip().split('\n')]
    )
    numbers.insert(0, 0)  # the socket is first device
    numbers.append(max(numbers) + 3)  # our device is the last

    differences = [numbers[i + 1] - numbers[i]
                   for i in range(len(numbers) - 1)]

    print(differences.count(1) * differences.count(3))


if __name__ == '__main__':
    main()
