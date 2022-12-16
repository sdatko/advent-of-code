#!/usr/bin/env python3
#
# --- Day 16: Proboscidea Volcanium ---
#
# The sensors have led you to the origin of the distress signal: yet another
# handheld device, just like the one the Elves gave you. However, you don't see
# any Elves around; instead, the device is surrounded by elephants! They must
# have gotten lost in these tunnels, and one of the elephants apparently
# figured out how to turn on the distress signal.
#
# The ground rumbles again, much stronger this time. What kind of cave is this,
# exactly? You scan the cave with your handheld device; it reports mostly
# igneous rock, some ash, pockets of pressurized gas, magma... this isn't
# just a cave, it's a volcano!
#
# You need to get the elephants out of here, quickly. Your device estimates
# that you have 30 minutes before the volcano erupts, so you don't have time
# to go back out the way you came in.
#
# You scan the cave for other options and discover a network of pipes
# and pressure-release valves. You aren't sure how such a system got into
# a volcano, but you don't have time to complain; your device produces a report
# (your puzzle input) of each valve's flow rate if it were opened (in pressure
# per minute) and the tunnels you could use to move between the valves.
#
# There's even a valve in the room you and the elephants are currently standing
# in labeled AA. You estimate it will take you one minute to open a single
# valve and one minute to follow any tunnel from one valve to another.
# What is the most pressure you could release?
#
# For example, suppose you had the following scan output:
#
#   Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
#   Valve BB has flow rate=13; tunnels lead to valves CC, AA
#   Valve CC has flow rate=2; tunnels lead to valves DD, BB
#   Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
#   Valve EE has flow rate=3; tunnels lead to valves FF, DD
#   Valve FF has flow rate=0; tunnels lead to valves EE, GG
#   Valve GG has flow rate=0; tunnels lead to valves FF, HH
#   Valve HH has flow rate=22; tunnel leads to valve GG
#   Valve II has flow rate=0; tunnels lead to valves AA, JJ
#   Valve JJ has flow rate=21; tunnel leads to valve II
#
# All of the valves begin closed. You start at valve AA, but it must be
# damaged or jammed or something: its flow rate is 0, so there's no point
# in opening it. However, you could spend one minute moving to valve BB
# and another minute opening it; doing so would release pressure during
# the remaining 28 minutes at a flow rate of 13, a total eventual pressure
# release of 28 * 13 = 364. Then, you could spend your third minute moving
# to valve CC and your fourth minute opening it, providing an additional
# 26 minutes of eventual pressure release at a flow rate of 2, or 52 total
# pressure released by valve CC.
#
# Making your way through the tunnels like this, you could probably open many
# or all of the valves by the time 30 minutes have elapsed. However, you need
# to release as much pressure as possible, so you'll need to be methodical.
# Instead, consider this approach:
#
#   == Minute 1 ==
#   No valves are open.
#   You move to valve DD.
#
#   == Minute 2 ==
#   No valves are open.
#   You open valve DD.
#
#   == Minute 3 ==
#   Valve DD is open, releasing 20 pressure.
#   You move to valve CC.
#
#   == Minute 4 ==
#   Valve DD is open, releasing 20 pressure.
#   You move to valve BB.
#
#   == Minute 5 ==
#   Valve DD is open, releasing 20 pressure.
#   You open valve BB.
#
#   == Minute 6 ==
#   Valves BB and DD are open, releasing 33 pressure.
#   You move to valve AA.
#
#   == Minute 7 ==
#   Valves BB and DD are open, releasing 33 pressure.
#   You move to valve II.
#
#   == Minute 8 ==
#   Valves BB and DD are open, releasing 33 pressure.
#   You move to valve JJ.
#
#   == Minute 9 ==
#   Valves BB and DD are open, releasing 33 pressure.
#   You open valve JJ.
#
#   == Minute 10 ==
#   Valves BB, DD, and JJ are open, releasing 54 pressure.
#   You move to valve II.
#
#   == Minute 11 ==
#   Valves BB, DD, and JJ are open, releasing 54 pressure.
#   You move to valve AA.
#
#   == Minute 12 ==
#   Valves BB, DD, and JJ are open, releasing 54 pressure.
#   You move to valve DD.
#
#   == Minute 13 ==
#   Valves BB, DD, and JJ are open, releasing 54 pressure.
#   You move to valve EE.
#
#   == Minute 14 ==
#   Valves BB, DD, and JJ are open, releasing 54 pressure.
#   You move to valve FF.
#
#   == Minute 15 ==
#   Valves BB, DD, and JJ are open, releasing 54 pressure.
#   You move to valve GG.
#
#   == Minute 16 ==
#   Valves BB, DD, and JJ are open, releasing 54 pressure.
#   You move to valve HH.
#
#   == Minute 17 ==
#   Valves BB, DD, and JJ are open, releasing 54 pressure.
#   You open valve HH.
#
#   == Minute 18 ==
#   Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
#   You move to valve GG.
#
#   == Minute 19 ==
#   Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
#   You move to valve FF.
#
#   == Minute 20 ==
#   Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
#   You move to valve EE.
#
#   == Minute 21 ==
#   Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
#   You open valve EE.
#
#   == Minute 22 ==
#   Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
#   You move to valve DD.
#
#   == Minute 23 ==
#   Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
#   You move to valve CC.
#
#   == Minute 24 ==
#   Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
#   You open valve CC.
#
#   == Minute 25 ==
#   Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
#   == Minute 26 ==
#   Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
#   == Minute 27 ==
#   Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
#   == Minute 28 ==
#   Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
#   == Minute 29 ==
#   Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
#   == Minute 30 ==
#   Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
# This approach lets you release the most pressure possible in 30 minutes
# with this valve layout, 1651.
#
# Work out the steps to release the most pressure in 30 minutes.
# What is the most pressure you can release?
#
#
# --- Solution ---
#
# We start by reading the input into a list of tuples, each containing a unique
# valve name/identifier, a pressure value at that valve and a list of neighbors
# reachable from that valve. This is achieved by removing unnecessary elements
# from the file content we read and splitting it over newlines and spaces.
# Then we convert everything into more helpful mappings/dictionaries:
# – the closes valves reachable from a given valves,
# – the pressures values at given valves,
# – the distances between given valves and their neighbors.
# The latter of the mentioned mappings is produced by iterating over the map
# of valves reachability using a BFS algorithm (breadth-first search) for each
# of the valves available. This way we build a graph of shortest distances.
# Then we traverse the graph, beginning at the given starting position and
# considering all moves to the valves that have a non-zero pressure value
# (movements between broken valves are possible, but they do not make any
# sense and skipping those valves greatly reduce the time it takes to find
# a solution). For every move, we reduce the available time limit and calculate
# how many pressure units would be released. Then we generate a new state to be
# analysed. If at any point we exceed the time limit or there are no more
# sensible valves to visit, then we save the current pressure value.
# Finally, as an answer, we return the biggest of saved values.
#

INPUT_FILE = 'input.txt'

START_POSITION = 'AA'
START_TIME = 30


def main():
    with open(INPUT_FILE, 'r') as file:
        valves = [valve.split()
                  for valve in file.read()
                                   .replace('Valve', '')
                                   .replace('has flow rate=', '')
                                   .replace('tunnels lead to valves', '')
                                   .replace('tunnel leads to valve', '')
                                   .replace(';', '')
                                   .replace(',', '')
                                   .strip()
                                   .split('\n')]

    distances = {}  # figured out below
    neighbors = {valve[0]: tuple(valve[2:]) for valve in valves}
    pressures = {valve[0]: int(valve[1]) for valve in valves
                 if valve[1] != '0'}

    for valve in neighbors.keys():
        positions = [valve]
        distances[valve] = {valve: 0}

        while positions:
            position = positions.pop(0)

            for neighbor in neighbors[position]:
                if neighbor not in distances[valve]:
                    distances[valve][neighbor] = distances[valve][position] + 1
                    positions.append(neighbor)

    max_pressure = 0
    states = [(START_POSITION, START_TIME, 0, set(pressures))]

    while states:
        state = states.pop()
        position, current_time, current_pressure, available_valves = state

        if not available_valves:
            if current_pressure > max_pressure:
                max_pressure = current_pressure
            continue

        for neighbor in available_valves:
            time_left = current_time - distances[position][neighbor] - 1

            if time_left <= 0:
                if current_pressure > max_pressure:
                    max_pressure = current_pressure
                continue

            valves_left = available_valves.copy()
            valves_left.remove(neighbor)

            new_pressure = current_pressure + time_left * pressures[neighbor]

            new_state = (neighbor, time_left, new_pressure, valves_left)
            states.append(new_state)

    print(max_pressure)


if __name__ == '__main__':
    main()
