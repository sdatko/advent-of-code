#!/usr/bin/env python3
#
# --- Day 16: Proboscidea Volcanium / Part Two ---
#
# You're worried that even with an optimal approach, the pressure released
# won't be enough. What if you got one of the elephants to help you?
#
# It would take you 4 minutes to teach an elephant how to open the right valves
# in the right order, leaving you with only 26 minutes to actually execute your
# plan. Would having two of you working together be better, even if it means
# having less time? (Assume that you teach the elephant before opening any
# valves yourself, giving you both the same full 26 minutes.)
#
# In the example above, you could teach the elephant to help you as follows:
#
#   == Minute 1 ==
#   No valves are open.
#   You move to valve II.
#   The elephant moves to valve DD.
#
#   == Minute 2 ==
#   No valves are open.
#   You move to valve JJ.
#   The elephant opens valve DD.
#
#   == Minute 3 ==
#   Valve DD is open, releasing 20 pressure.
#   You open valve JJ.
#   The elephant moves to valve EE.
#
#   == Minute 4 ==
#   Valves DD and JJ are open, releasing 41 pressure.
#   You move to valve II.
#   The elephant moves to valve FF.
#
#   == Minute 5 ==
#   Valves DD and JJ are open, releasing 41 pressure.
#   You move to valve AA.
#   The elephant moves to valve GG.
#
#   == Minute 6 ==
#   Valves DD and JJ are open, releasing 41 pressure.
#   You move to valve BB.
#   The elephant moves to valve HH.
#
#   == Minute 7 ==
#   Valves DD and JJ are open, releasing 41 pressure.
#   You open valve BB.
#   The elephant opens valve HH.
#
#   == Minute 8 ==
#   Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
#   You move to valve CC.
#   The elephant moves to valve GG.
#
#   == Minute 9 ==
#   Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
#   You open valve CC.
#   The elephant moves to valve FF.
#
#   == Minute 10 ==
#   Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
#   The elephant moves to valve EE.
#
#   == Minute 11 ==
#   Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
#   The elephant opens valve EE.
#
#   (At this point, all valves are open.)
#
#   == Minute 12 ==
#   Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
#   ...
#
#   == Minute 20 ==
#   Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
#   ...
#
#   == Minute 26 ==
#   Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
#
# With the elephant helping, after 26 minutes, the best you could do
# would release a total of 1707 pressure.
#
# With you and an elephant working together for 26 minutes,
# what is the most pressure you could release?
#
#
# --- Solution ---
#
# The difference here is that the time limit is shorter, but there are two
# individuals to be considered that are moving independently in our graph.
# The key to reach a solution was to realise that the two individuals
# can visit a different number of valves (i.e. one may finish just after
# visiting a single valve, while the other may visit five valves).
# Therefore, to find a solution, we record the information about the highest
# possible pressure value we can get after visiting a given set of valves.
# In other words, we produce all possible sub-solutions to the problem.
# Then what is needed is to browse all the possible pairs of sub-solutions
# that contain disjoint lists of valves visited (i.e. empty intersection)
# to discover the highest value we can reach.
#

INPUT_FILE = 'input.txt'

START_POSITION = 'AA'
START_TIME = 26


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

    reached_pressures = {}
    states = [(START_POSITION, START_TIME, 0, set(pressures))]

    while states:
        state = states.pop()
        position, current_time, current_pressure, available_valves = state

        key = tuple(sorted(set(pressures) - available_valves))
        if reached_pressures.get(key, 0) < current_pressure:
            reached_pressures[key] = current_pressure

        if not available_valves:
            continue

        for neighbor in available_valves:
            time_left = current_time - distances[position][neighbor] - 1

            if time_left <= 0:
                continue

            valves_left = available_valves.copy()
            valves_left.remove(neighbor)

            new_pressure = current_pressure + time_left * pressures[neighbor]

            new_state = (neighbor, time_left, new_pressure, valves_left)
            states.append(new_state)

    max_pressure = 0
    complementary_pressures = list(reached_pressures.keys())

    for solution1 in reached_pressures:
        complementary_pressures.remove(solution1)

        for solution2 in complementary_pressures:
            if not (set(solution1) & set(solution2)):
                total = reached_pressures[solution1]
                total += reached_pressures[solution2]

                if total > max_pressure:
                    max_pressure = total

    print(max_pressure)


if __name__ == '__main__':
    main()
