#!/usr/bin/env python3
#
# --- Day 12: Passage Pathing ---
#
# With your submarine's subterranean subsystems subsisting suboptimally,
# the only way you're getting out of this cave anytime soon is by finding
# a path yourself. Not just a path - the only way to know if you've found
# the best path is to find all of them.
#
# Fortunately, the sensors are still mostly working, and so you build a rough
# map of the remaining caves (your puzzle input). For example:
#   start-A
#   start-b
#   A-c
#   A-b
#   b-d
#   A-end
#   b-end
#
# This is a list of how all of the caves are connected. You start in the cave
# named start, and your destination is the cave named end. An entry like
# b-d means that cave b is connected to cave d - that is, you can move
# between them.
#
# So, the above cave system looks roughly like this:
#       start
#       /   \
#   c--A-----b--d
#       \   /
#        end
#
# Your goal is to find the number of distinct paths that start at start,
# end at end, and don't visit small caves more than once. There are two types
# of caves: big caves (written in uppercase, like A) and small caves (written
# in lowercase, like b). It would be a waste of time to visit any small cave
# more than once, but big caves are large enough that it might be worth
# visiting them multiple times. So, all paths you find should visit small
# caves at most once, and can visit big caves any number of times.
#
# Given these rules, there are 10 paths through this example cave system:
# - start,A,b,A,c,A,end
# - start,A,b,A,end
# - start,A,b,end
# - start,A,c,A,b,A,end
# - start,A,c,A,b,end
# - start,A,c,A,end
# - start,A,end
# - start,b,A,c,A,end
# - start,b,A,end
# - start,b,end
#
# (Each line in the above list corresponds to a single path; the caves
# visited by that path are listed in the order they are visited and
# separated by commas.)
#
# Note that in this cave system, cave d is never visited by any path:
# to do so, cave b would need to be visited twice (once on the way to cave
# d and a second time when returning from cave d), and since cave b is small,
# this is not allowed.
#
# Here is a slightly larger example:
#   dc-end
#   HN-start
#   start-kj
#   dc-start
#   dc-HN
#   LN-dc
#   HN-end
#   kj-sa
#   kj-HN
#   kj-dc
#
# The 19 paths through it are as follows:
# - start,HN,dc,HN,end
# - start,HN,dc,HN,kj,HN,end
# - start,HN,dc,end
# - start,HN,dc,kj,HN,end
# - start,HN,end
# - start,HN,kj,HN,dc,HN,end
# - start,HN,kj,HN,dc,end
# - start,HN,kj,HN,end
# - start,HN,kj,dc,HN,end
# - start,HN,kj,dc,end
# - start,dc,HN,end
# - start,dc,HN,kj,HN,end
# - start,dc,end
# - start,dc,kj,HN,end
# - start,kj,HN,dc,HN,end
# - start,kj,HN,dc,end
# - start,kj,HN,end
# - start,kj,dc,HN,end
# - start,kj,dc,end
#
# Finally, this even larger example has 226 paths through it:
#   fs-end
#   he-DX
#   fs-he
#   start-DX
#   pj-DX
#   end-zg
#   zg-sl
#   zg-pj
#   pj-he
#   RW-he
#   fs-DX
#   pj-RW
#   zg-RW
#   start-pj
#   he-WI
#   zg-he
#   pj-fs
#   start-RW
#
# How many paths through this cave system are there that visit small caves
# at most once?
#
#
# --- Solution ---
#
# We start by reading the list of edges from input file and preparing,
# for convenience, a dictionary that will give us list of all possible edges
# from a specified cave. Then we aim to check all possible paths from a given
# starting point, counting those that take us to the goal (end). So we define
# a list of paths with initial entry – single path with just one element,
# the starting location. Then we perform a loop as long as there are still
# some paths to consider (our list of paths is not empty). In each iteration,
# we take the first path from the list of paths, we look at the last element
# in that taken path (i.e. the current cave we reached) and we find all next
# caves that are reachable from that point. For each of possible next caves:
# - if the next cave is our goal (end), we count we found one possible solution
#   and do nothing else,
# - if the next cave is written with lowercase letters and it was already
#   visited (there is already such element in our path), we skip this one
#   as it is forbidden location now (note that the 'start' also fits this
#   condition, so we have no moving back and forth between A and start),
# - otherwise we produce a new path to consider by adding next cave to current
#   list and we add it to the list of paths we check.
# With a rule that visiting some caves twice is forbidden, this look through
# all possible paths eventually comes to and end (actually, it is quite fast).
# As final result, we just print the counter of solutions we found.
#

INPUT_FILE = 'input.txt'


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
        path = paths.pop(0)
        last_cave = path[-1]

        for next_cave in connections[last_cave]:
            if next_cave == goal:
                possible_paths += 1
                continue

            if next_cave.islower() and path.count(next_cave):
                continue

            new_path = path + [next_cave]
            paths.append(new_path)

    print(possible_paths)


if __name__ == '__main__':
    main()
