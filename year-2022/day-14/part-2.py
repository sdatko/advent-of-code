#!/usr/bin/env python3
#
# --- Day 14: Regolith Reservoir / Part Two ---
#
# You realize you misread the scan. There isn't an endless void at the bottom
# of the scan - there's floor, and you're standing on it!
#
# You don't have time to scan the floor, so assume the floor is an infinite
# horizontal line with a y coordinate equal to two plus the highest
# y coordinate of any point in your scan.
#
# In the example above, the highest y coordinate of any point is 9,
# and so the floor is at y=11. (This is as if your scan contained one extra
# rock path like -infinity,11 -> infinity,11.)
#
# With the added floor, the example above now looks like this:
#
#           ...........+........
#           ....................
#           ....................
#           ....................
#           .........#...##.....
#           .........#...#......
#           .......###...#......
#           .............#......
#           .............#......
#           .....#########......
#           ....................
#   <-- etc #################### etc -->
#
# To find somewhere safe to stand, you'll need to simulate falling sand
# until a unit of sand comes to rest at 500,0, blocking the source entirely
# and stopping the flow of sand into the cave. In the example above,
# the situation finally looks like this after 93 units of sand come to rest:
#
#   ............o............
#   ...........ooo...........
#   ..........ooooo..........
#   .........ooooooo.........
#   ........oo#ooo##o........
#   .......ooo#ooo#ooo.......
#   ......oo###ooo#oooo......
#   .....oooo.oooo#ooooo.....
#   ....oooooooooo#oooooo....
#   ...ooo#########ooooooo...
#   ..ooooo.......ooooooooo..
#   #########################
#
# Using your scan, simulate the falling sand until the source of the sand
# becomes blocked. How many units of sand come to rest?
#
#
# --- Solution ---
#
# The difference in this part is the end condition for our simulation.
# Now we finish, when the last placed grain of sand is at its initial position.
# To make the falling finite, we put additional condition that we can move
# down only as long as we did not reach the lever/layer two positions further
# than the last line of rocks (max `y` from the initial sequences).
# The rest of the code remains basically the same, though I also added
# a function to draw the visualization of rock and sand.
#

INPUT_FILE = 'input.txt'

START_X = 500
START_Y = 0


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def draw(obstacles: set, rocks: set) -> None:
    min_x = min([point[0] for point in obstacles])
    max_x = max([point[0] for point in obstacles])
    max_y = max([point[1] for point in obstacles])

    for y in range(0, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in rocks:
                print('#', end='')
            elif (x, y) in obstacles:
                print('o', end='')
            else:
                print(' ', end='')
        print()  # line break


def main():
    with open(INPUT_FILE, 'r') as file:
        sequences = [[tuple(map(int, point.split(',')))
                      for point in sequence.split(' -> ')]
                     for sequence in file.read().strip().split('\n')]

    obstacles = set()

    for sequence in sequences:
        for start, end in zip(sequence[:-1], sequence[1:]):
            x1, y1 = start
            x2, y2 = end
            dx = sign(x2 - x1)
            dy = sign(y2 - y1)

            obstacles.add((x1, y1))

            while x1 != x2 or y1 != y2:
                x1 += dx
                y1 += dy
                obstacles.add((x1, y1))

    count = 0
    max_y = max([point[1] for point in obstacles]) + 2
    # rocks = obstacles.copy()

    while True:
        grain_x, grain_y = (START_X, START_Y)

        while True:
            # It is only possible to move as long as we will not hit the floor
            if (grain_y + 1) < max_y:

                # Fall until there is a space below
                if (grain_x, grain_y + 1) not in obstacles:
                    grain_y += 1
                    continue

                # Check if there is free space on the left
                if (grain_x - 1, grain_y + 1) not in obstacles:
                    grain_x -= 1
                    grain_y += 1
                    continue

                # Check if there is free space on the right
                if (grain_x + 1, grain_y + 1) not in obstacles:
                    grain_x += 1
                    grain_y += 1
                    continue

            # Otherwise, put the grain where it landed
            obstacles.add((grain_x, grain_y))
            count += 1
            break

        # Break if we are unable to move
        if (grain_x, grain_y) == (START_X, START_Y):
            break

    # draw(obstacles, rocks)
    print(count)


if __name__ == '__main__':
    main()
