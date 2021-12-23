#!/usr/bin/env python3
#
# Task:
# As you prepare to give the amphipods your solution, you notice that
# the diagram they handed you was actually folded up. As you unfold it,
# you discover an extra part of the diagram.
# Between the first and second lines of text that contain amphipod starting
# positions, insert the following lines:
#   #D#C#B#A#
#   #D#B#A#C#
# So, the above example now becomes:
#   #############
#   #...........#
#   ###B#C#B#D###
#     #D#C#B#A#
#     #D#B#A#C#
#     #A#D#C#A#
#     #########
# The amphipods still want to be organized into rooms similar to before:
#   #############
#   #...........#
#   ###A#B#C#D###
#     #A#B#C#D#
#     #A#B#C#D#
#     #A#B#C#D#
#     #########
# In this updated example, the least energy required to organize these
# amphipods is 44169:
#   #############
#   #...........#
#   ###B#C#B#D###
#     #D#C#B#A#
#     #D#B#A#C#
#     #A#D#C#A#
#     #########
#
#   #############
#   #..........D#
#   ###B#C#B#.###
#     #D#C#B#A#
#     #D#B#A#C#
#     #A#D#C#A#
#     #########
#
#   #############
#   #A.........D#
#   ###B#C#B#.###
#     #D#C#B#.#
#     #D#B#A#C#
#     #A#D#C#A#
#     #########
#
#   #############
#   #A........BD#
#   ###B#C#.#.###
#     #D#C#B#.#
#     #D#B#A#C#
#     #A#D#C#A#
#     #########
#
#   #############
#   #A......B.BD#
#   ###B#C#.#.###
#     #D#C#.#.#
#     #D#B#A#C#
#     #A#D#C#A#
#     #########
#
#   #############
#   #AA.....B.BD#
#   ###B#C#.#.###
#     #D#C#.#.#
#     #D#B#.#C#
#     #A#D#C#A#
#     #########
#
#   #############
#   #AA.....B.BD#
#   ###B#.#.#.###
#     #D#C#.#.#
#     #D#B#C#C#
#     #A#D#C#A#
#     #########
#
#   #############
#   #AA.....B.BD#
#   ###B#.#.#.###
#     #D#.#C#.#
#     #D#B#C#C#
#     #A#D#C#A#
#     #########
#
#   #############
#   #AA...B.B.BD#
#   ###B#.#.#.###
#     #D#.#C#.#
#     #D#.#C#C#
#     #A#D#C#A#
#     #########
#
#   #############
#   #AA.D.B.B.BD#
#   ###B#.#.#.###
#     #D#.#C#.#
#     #D#.#C#C#
#     #A#.#C#A#
#     #########
#
#   #############
#   #AA.D...B.BD#
#   ###B#.#.#.###
#     #D#.#C#.#
#     #D#.#C#C#
#     #A#B#C#A#
#     #########
#
#   #############
#   #AA.D.....BD#
#   ###B#.#.#.###
#     #D#.#C#.#
#     #D#B#C#C#
#     #A#B#C#A#
#     #########
#
#   #############
#   #AA.D......D#
#   ###B#.#.#.###
#     #D#B#C#.#
#     #D#B#C#C#
#     #A#B#C#A#
#     #########
#
#   #############
#   #AA.D......D#
#   ###B#.#C#.###
#     #D#B#C#.#
#     #D#B#C#.#
#     #A#B#C#A#
#     #########
#
#   #############
#   #AA.D.....AD#
#   ###B#.#C#.###
#     #D#B#C#.#
#     #D#B#C#.#
#     #A#B#C#.#
#     #########
#
#   #############
#   #AA.......AD#
#   ###B#.#C#.###
#     #D#B#C#.#
#     #D#B#C#.#
#     #A#B#C#D#
#     #########
#
#   #############
#   #AA.......AD#
#   ###.#B#C#.###
#     #D#B#C#.#
#     #D#B#C#.#
#     #A#B#C#D#
#     #########
#
#   #############
#   #AA.......AD#
#   ###.#B#C#.###
#     #.#B#C#.#
#     #D#B#C#D#
#     #A#B#C#D#
#     #########
#
#   #############
#   #AA.D.....AD#
#   ###.#B#C#.###
#     #.#B#C#.#
#     #.#B#C#D#
#     #A#B#C#D#
#     #########
#
#   #############
#   #A..D.....AD#
#   ###.#B#C#.###
#     #.#B#C#.#
#     #A#B#C#D#
#     #A#B#C#D#
#     #########
#
#   #############
#   #...D.....AD#
#   ###.#B#C#.###
#     #A#B#C#.#
#     #A#B#C#D#
#     #A#B#C#D#
#     #########
#
#   #############
#   #.........AD#
#   ###.#B#C#.###
#     #A#B#C#D#
#     #A#B#C#D#
#     #A#B#C#D#
#     #########
#
#   #############
#   #..........D#
#   ###A#B#C#.###
#     #A#B#C#D#
#     #A#B#C#D#
#     #A#B#C#D#
#     #########
#
#   #############
#   #...........#
#   ###A#B#C#D###
#     #A#B#C#D#
#     #A#B#C#D#
#     #A#B#C#D#
#     #########
# Using the initial configuration from the full diagram, what is the least
# energy required to organize the amphipods?
#
# Solution:
# Similar approach (solution by hand) worked here after a few trials. However,
# I wanted to implement a general solution here, as the challenge is called
# Advent of *Code*. So, the idea is to browse states-space, where the state
# represents the arrangement of elements in the corridor and rooms, starting
# with initial state read from the input file. In a loop, as long as there are
# states still to browse, we perform the following actions:
# - we take the state with currently the lowest energy cost,
# - we check if current state is a solved one – if so, we finish;
# - otherwise we find all possible moves in current state and generate
#   new states to browse.
# The current state is solved, when every room contains only the desired
# elements on their target positions (i.e. there is A,B,C,D in each row).
# For finding the possible moves, there are two separate variants to consider.
# Each element from a corridor can move *only* to its target room. The move
# is only possible when the path is clear (no intermediate positions occupied)
# and in target room there are no unwanted elements (other than the desired
# or empty spaces). On the other hand, each element currently in a room, can be
# moved to any unoccupied place in corridor that is not directly next to room
# (forbidden positions), provided that there is a clear path (no intermediate
# positions occupied). Additionally from a room we cannot move elements that
# are already properly arranged (i.e. given element and *all beneath it* are
# in their target room). We also do not move elements that are not on top of
# the room (there is no empty space above the element).
# To generate new states we need to deepcopy a list (inspiration from Day 18)
# and to find quickly the state of lowest current cost we use a heap (based
# on implementation from Day 15).
# This quickly generates hundreds of thousands of new states to browse. However
# it may be noticed, that many states are actually a duplicates, as we do not
# distinguish between the same elements (such as A and A) on various positions.
# Considering the first example of part 1:
#   #############
#   #...........#
#   ###B#C#B#D###
#     #A#D#C#A#
#     #########
# We may move element B from room 1 to position 2 in corridor and element B
# from room 3 to position 8 in corridor, for total cost of 2 * 10 + 2 * 10.
# The outcome is then as follows:
#   #############
#   #.B.....B...#
#   ###.#C#.#D###
#     #A#D#C#A#
#     #########
# However, the same state, as we do not distinguish elements, can be achieved
# by different moves – element B from room 3 can be moved to position 2 and
# element B from from room 1 can be moved to position 8. The outcome looks
# the same, though the energy cost this time is greater: 6 * 10 + 6 * 10.
# Because we process the states ordered by energy cost, if we will ever reach
# a state that was already seen, the new state must be of greater cost than
# the previously seen (actually, at best, it may be the same). It means this
# new state will lead to the same next states as the previously seen state did,
# but their cost will be also greater. There is then no point in considering
# this state and any further state it may generate, as we already saw the same
# or better way to reach this state (in terms of energy cost) and we can skip
# the processing. This greatly reduces the number of states to browse and
# allows to find the answer in a few seconds.
#

INPUT_FILE = 'input.txt'

COSTS = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

GOAL_ROOMS = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
}

ROOM_CORRIDOR = {
    0: 2,
    1: 4,
    2: 6,
    3: 8,
}

FORBIDDEN = tuple(ROOM_CORRIDOR.values())


def heapify(array, index=0):
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < len(array) and array[left][0] < array[smallest][0]:
        smallest = left

    if right < len(array) and array[right][0] < array[smallest][0]:
        smallest = right

    if smallest != index:
        array[index], array[smallest] = array[smallest], array[index]
        heapify(array, smallest)


def heap_pop(array):
    root = array[0]
    array[0] = array[len(array) - 1]
    array.pop()
    heapify(array)
    return root


def heap_push(array, element):
    array.append(element)
    index = len(array) - 1
    parent = (index - 1) // 2

    while index != 0 and array[parent][0] > array[index][0]:
        array[index], array[parent] = array[parent], array[index]
        index = parent
        parent = (index - 1) // 2


def deepcopy(deeplist):
    new_list = []
    for row in deeplist:
        new_list.append(row.copy())
    return new_list


def tuplify(state):
    corridor, rooms = state
    corridor = tuple(corridor)
    rooms = tuple([tuple(row) for row in rooms])
    return tuple([corridor, rooms])


def find_all_possible_moves(states, cost, corridor, rooms):
    find_all_moves_from_corridor(states, cost, corridor, rooms)
    find_all_moves_to_corridor(states, cost, corridor, rooms)


def find_all_moves_from_corridor(states, cost, corridor, rooms):
    for position, element in enumerate(corridor):
        if not element:
            continue

        target_room_index = GOAL_ROOMS[element]
        target_room_position = ROOM_CORRIDOR[GOAL_ROOMS[element]]

        indexes = (position, target_room_position)
        index1 = min(indexes)
        index2 = max(indexes)

        # exclude the current position from range
        if index1 == position:
            index1 += 1
        else:
            index2 -= 1

        if any(corridor[index1:index2]):
            continue  # intermediate position occupied, cannot move

        if any([room[target_room_index] not in [element, None]
                for room in rooms]):
            continue  # room contains unwanted elements

        target_row_index = max([index for index in range(len(rooms))
                                if rooms[index][target_room_index] is None])

        distance = index2 - index1 + target_row_index + 1
        distance += 1  # include the skipped position in range
        new_cost = cost + distance * COSTS[element]

        new_corridor = corridor.copy()
        new_rooms = deepcopy(rooms)

        new_corridor[position] = None
        new_rooms[target_row_index][target_room_index] = element
        new_state = (new_corridor, new_rooms)

        heap_push(states, (new_cost, new_state))


def find_all_moves_to_corridor(states, cost, corridor, rooms):
    for row_index, row in enumerate(rooms):
        for room_index, element in enumerate(row):
            if element is None:
                continue  # empty room

            if row_index > 0 and rooms[row_index - 1][room_index] is not None:
                continue  # no empty room above the element

            if all([room_index == GOAL_ROOMS[room[room_index]]
                    for room in rooms[row_index:]]):
                continue  # current and below elements are at correct position

            for candidate in range(len(corridor)):
                if candidate in FORBIDDEN:
                    continue  # cannot move to that position (next to room)

                if corridor[candidate] is not None:
                    continue  # position already occupied

                indexes = (candidate, ROOM_CORRIDOR[room_index])
                index1 = min(indexes)
                index2 = max(indexes)
                if any(corridor[index1:index2]):
                    continue  # intermediate position occupied, cannot move

                distance = index2 - index1 + row_index + 1
                new_cost = cost + distance * COSTS[element]

                new_corridor = corridor.copy()
                new_rooms = deepcopy(rooms)

                new_corridor[candidate] = element
                new_rooms[row_index][room_index] = None
                new_state = (new_corridor, new_rooms)

                heap_push(states, (new_cost, new_state))


def solved(rooms):
    for row in rooms:
        if row != ['A', 'B', 'C', 'D']:
            return False
    return True


def main():
    with open(INPUT_FILE, 'r') as file:
        rooms = [list(line.strip().replace('#', ''))
                 for line in file.readlines()
                 if ('A' in line) or ('B' in line) or ('C' in line)]
    corridor = [None] * 11

    rooms.insert(1, ['D', 'C', 'B', 'A'])
    rooms.insert(2, ['D', 'B', 'A', 'C'])

    def print_status():  # for debugging
        print(str(corridor).replace(', ', '')
                           .replace('None', '.').replace("'", '')
                           .replace('[', '').replace(']', ''))
        print(str(rooms).replace('],', '],\n').replace(',', '')
                        .replace('None', '.').replace("'", '')
                        .replace('[', ' ').replace(']', ''))

    initial_cost = 0
    initial_state = (corridor, rooms)
    states = [(initial_cost, initial_state)]

    states_seen = set()

    while states:
        cost, state = heap_pop(states)
        corridor, rooms = state

        state_hash = tuplify(state)
        if state_hash in states_seen:
            continue
        states_seen.add(state_hash)

        if solved(rooms):
            break
        else:
            find_all_possible_moves(states, cost, corridor, rooms)

    print(cost)


if __name__ == '__main__':
    main()
