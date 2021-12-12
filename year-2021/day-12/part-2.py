#!/usr/bin/env python3
#
# Task:
# After reviewing the available paths, you realize you might have time
# to visit a single small cave twice. Specifically, big caves can be visited
# any number of times, a single small cave can be visited at most twice, and
# the remaining small caves can be visited at most once. However, the caves
# named start and end can only be visited exactly once each: once you leave
# the start cave, you may not return to it, and once you reach the end cave,
# the path must end immediately.
# Given these new rules, how many paths through this cave system are there?
#
# Solution:
# The only change in this part is related to the definition of forbidden
# locations. We add additional check – if the next cave is our starting point,
# we skip that path. Then we modify the case for small caves (i.e. with names
# written using lowercase letters) – now if the next cave was already visited
# two times, or it was visited once but there was already any small cave
# visited twice, we skip it.
#

INPUT_FILE = 'input.txt'


def visited_small_cave_twice(path: list) -> bool:
    for cave in path:
        if cave.islower() and path.count(cave) >= 2:
            return True
    return False


def main():
    edges = [line.strip().split('-') for line in open(INPUT_FILE, 'r')]

    connections = {}

    for edge in edges:
        start, end = edge

        if start not in connections:
            connections[start] = set()
        if end not in connections:
            connections[end] = set()

        connections[start].add(end)
        connections[end].add(start)

    goal = 'end'
    paths = [['start']]
    possible_paths = 0

    while paths:
        path = paths.pop()
        last_cave = path[-1]

        for next_cave in connections[last_cave]:
            if next_cave == goal:
                possible_paths += 1
                continue

            if next_cave == path[0]:
                continue

            if next_cave.islower():
                if path.count(next_cave) >= 2:
                    continue

                if path.count(next_cave) and visited_small_cave_twice(path):
                    continue

            new_path = path + [next_cave]
            paths.append(new_path)

    print(possible_paths)


if __name__ == '__main__':
    main()
