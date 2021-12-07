#!/usr/bin/env python3
#
# Task:
# A giant whale has decided your submarine is its next meal, and it's much
# faster than you are. There's nowhere to run!
# Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep
# for them otherwise) zooms in to rescue you! They seem to be preparing to
# blast a hole in the ocean floor; sensors indicate a massive underground
# cave system just beyond where they're aiming!
# The crab submarines all need to be aligned before they'll have enough power
# to blast a large enough hole for your submarine to get through. However,
# it doesn't look like they'll be aligned before the whale catches you!
# Maybe you can help?
# There's one major catch - crab submarines can only move horizontally.
# You quickly make a list of the horizontal position of each crab (your puzzle
# input). Crab submarines have limited fuel, so you need to find a way to make
# all of their horizontal positions match while requiring them to spend as
# little fuel as possible.
# Each change of 1 step in horizontal position of a single crab costs 1 fuel.
# You could choose any horizontal position to align them all on, but there is
# one that costs the least fuel.
# Determine the horizontal position that the crabs can align to using the least
# fuel possible. How much fuel must they spend to align to that position?
#
# Solution:
# We read the input as comma separated values, treating elements as integers.
# Then we take the pretty much straightforward approach – we try the positions
# from minimum to maximum of our array, for each one calculating the absolute
# differences with our array elements (ie. how much each crab submarine will
# have to move). We obtain the fuel cost by finding the sum of array elements
# and we save the smallest one we can find.
# Probably the solution can be found with more direct approach. Experimenting
# I found that for both example and puzzle input, the optimal position can be
# around median of initial positions (sorted(positions)[len(positions) // 2]),
# however I cannot justify than and I am not sure it works for all cases.
#

INPUT_FILE = 'input.txt'


def main():
    positions = [int(number)
                 for line in open(INPUT_FILE, 'r')
                 for number in line.strip().split(',')]

    fuel_cost = sum(positions)

    for new_position in range(min(positions), max(positions)):
        costs = [abs(current_position - new_position)
                 for current_position in positions]
        new_cost = sum(costs)

        if new_cost < fuel_cost:
            fuel_cost = new_cost

    print(fuel_cost)


if __name__ == '__main__':
    main()
