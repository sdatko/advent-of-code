#!/usr/bin/env python3
#
# --- Day 24: Blizzard Basin / Part Two ---
#
# As the expedition reaches the far side of the valley,
# one of the Elves looks especially dismayed:
#
# He forgot his snacks at the entrance to the valley!
#
# Since you're so good at dodging blizzards, the Elves humbly request that
# you go back for his snacks. From the same initial conditions, how quickly
# can you make it from the start to the goal, then back to the start, then
# back to the goal?
#
# In the above example, the first trip to the goal takes 18 minutes,
# the trip back to the start takes 23 minutes, and the trip back to the goal
# again takes 13 minutes, for a total time of 54 minutes.
#
# What is the fewest number of minutes required to reach the goal, go back
# to the start, then reach the goal again?
#
#
# --- Solution ---
#
# The difference here is that we now need to perform two additional transitions
# through the maze. Hence, the originally developed algorithm was converted
# to a function that takes the beginning and target positions as arguments,
# as well as the map of the maze with winds. It returns the smallest number
# of steps / time units required to pass through the maze, as well as the new
# state of the maze (wind positions) after that time. Then we simply call
# that function 3 times and we sum the results to find the total duration.
# Note that additional check was necessary when finding all reachable places,
# as now, when starting from the original goal, it is possible to encounter
# the out of bounds exception.
#

INPUT_FILE = 'input.txt'


def deepcopy(deeplist):
    new_list = []
    for row in deeplist:
        new_list.append(row.copy())
    return new_list


def find_transition_time(start, goal, grid):
    clean_grid = deepcopy(grid)
    for y, row in enumerate(grid[1:-1], start=1):
        for x, tile in enumerate(row[1:-1], start=1):
            clean_grid[y][x] = 0

    min_x = 1
    min_y = 1
    max_x = len(grid[0]) - 2
    max_y = len(grid) - 2

    reached_positions = {start}
    time = 0

    while goal not in reached_positions:
        time += 1

        # move winds
        new_grid = deepcopy(clean_grid)

        for y, row in enumerate(grid[1:-1], start=1):
            for x, tile in enumerate(row[1:-1], start=1):
                # up
                if grid[y][x] & 1:
                    if y > min_y:
                        ny = y - 1
                    else:
                        ny = max_y
                    new_grid[ny][x] += 1

                # down
                if grid[y][x] & 2:
                    if y < max_y:
                        ny = y + 1
                    else:
                        ny = min_y
                    new_grid[ny][x] += 2

                # left
                if grid[y][x] & 4:
                    if x > min_x:
                        nx = x - 1
                    else:
                        nx = max_x
                    new_grid[y][nx] += 4

                # right
                if grid[y][x] & 8:
                    if x < max_x:
                        nx = x + 1
                    else:
                        nx = min_y
                    new_grid[y][nx] += 8

        grid = new_grid

        # find reachable positions
        new_positions = set()

        for y, x in reached_positions:
            for ny, nx in ((y - 1, x),  # up
                           (y + 1, x),  # down
                           (y, x - 1),  # left
                           (y, x + 1),  # right
                           (y, x)):  # wait in place
                if ny >= len(grid):
                    continue
                if new_grid[ny][nx] != 0:
                    continue

                new_positions.add((ny, nx))

        reached_positions = new_positions

    return time, grid


def main():
    with open(INPUT_FILE, 'r') as file:
        grid = [list(map(int, row.strip().split()))
                for row in file.read()
                               .replace('.', '0 ')
                               .replace('^', '1 ')
                               .replace('v', '2 ')
                               .replace('<', '4 ')
                               .replace('>', '8 ')
                               .replace('#', '16 ')
                               .strip()
                               .split('\n')]

    start = (0, grid[0].index(0))
    goal = (len(grid) - 1, grid[-1].index(0))

    time1, grid = find_transition_time(start, goal, grid)
    time2, grid = find_transition_time(goal, start, grid)
    time3, grid = find_transition_time(start, goal, grid)

    print(time1 + time2 + time3)


if __name__ == '__main__':
    main()
