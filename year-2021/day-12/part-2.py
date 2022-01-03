#!/usr/bin/env python3
#
# --- Day 12: Passage Pathing / Part Two ---
#
# After reviewing the available paths, you realize you might have time
# to visit a single small cave twice. Specifically, big caves can be visited
# any number of times, a single small cave can be visited at most twice, and
# the remaining small caves can be visited at most once. However, the caves
# named start and end can only be visited exactly once each: once you leave
# the start cave, you may not return to it, and once you reach the end cave,
# the path must end immediately.
#
# Now, the 36 possible paths through the first example above are:
#   start,A,b,A,b,A,c,A,end
#   start,A,b,A,b,A,end
#   start,A,b,A,b,end
#   start,A,b,A,c,A,b,A,end
#   start,A,b,A,c,A,b,end
#   start,A,b,A,c,A,c,A,end
#   start,A,b,A,c,A,end
#   start,A,b,A,end
#   start,A,b,d,b,A,c,A,end
#   start,A,b,d,b,A,end
#   start,A,b,d,b,end
#   start,A,b,end
#   start,A,c,A,b,A,b,A,end
#   start,A,c,A,b,A,b,end
#   start,A,c,A,b,A,c,A,end
#   start,A,c,A,b,A,end
#   start,A,c,A,b,d,b,A,end
#   start,A,c,A,b,d,b,end
#   start,A,c,A,b,end
#   start,A,c,A,c,A,b,A,end
#   start,A,c,A,c,A,b,end
#   start,A,c,A,c,A,end
#   start,A,c,A,end
#   start,A,end
#   start,b,A,b,A,c,A,end
#   start,b,A,b,A,end
#   start,b,A,b,end
#   start,b,A,c,A,b,A,end
#   start,b,A,c,A,b,end
#   start,b,A,c,A,c,A,end
#   start,b,A,c,A,end
#   start,b,A,end
#   start,b,d,b,A,c,A,end
#   start,b,d,b,A,end
#   start,b,d,b,end
#   start,b,end
#
# The slightly larger example above now has 103 paths through it,
# and the even larger example now has 3509 paths through it.
#
# Given these new rules, how many paths through this cave system are there?
#
#
# --- Solution ---
#
# The only change in this part is related to the definition of forbidden
# locations. We add additional check – if the next cave is our starting point,
# we skip that path. Then we modify the case for small caves (i.e. with names
# written using lowercase letters) – now if the next cave was not visited yet
# we produce new path for it, otherwise we only use it as part of new path
# only if there was no cave visited second time so far (for this, we introduce
# additional variable that stores the information about that). In case of
# big caves we add them always to the path.
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
    paths = [(['start'], False)]
    possible_paths = 0

    while paths:
        path, anything_visited_twice = paths.pop()
        last_cave = path[-1]

        for next_cave in connections[last_cave]:
            if next_cave == goal:
                possible_paths += 1
                continue

            if next_cave == path[0]:
                continue

            if next_cave.islower():
                if next_cave not in path:
                    new_path = (path + [next_cave], anything_visited_twice)
                    paths.append(new_path)

                elif not anything_visited_twice:
                    new_path = (path + [next_cave], True)
                    paths.append(new_path)

            else:
                new_path = (path + [next_cave], anything_visited_twice)
                paths.append(new_path)

    print(possible_paths)


if __name__ == '__main__':
    main()
