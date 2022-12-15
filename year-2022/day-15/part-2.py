#!/usr/bin/env python3
#
# --- Day 15: Beacon Exclusion Zone / Part Two ---
#
# Your handheld device indicates that the distress signal is coming from
# a beacon nearby. The distress beacon is not detected by any sensor, but
# the distress beacon must have x and y coordinates each no lower than 0
# and no larger than 4000000.
#
# To isolate the distress beacon's signal, you need to determine its tuning
# frequency, which can be found by multiplying its x coordinate by 4000000
# and then adding its y coordinate.
#
# In the example above, the search space is smaller: instead, the x and y
# coordinates can each be at most 20. With this reduced search area,
# there is only a single position that could have a beacon: x=14, y=11.
# The tuning frequency for this distress beacon is 56000011.
#
# Find the only possible position for the distress beacon.
# What is its tuning frequency?
#
#
# --- Solution ---
#
# In this part I took a little different assumption. Expecting that
# in the whole range <0; 4000000>, between numerous sensors and beacons,
# there is exactly one unoccupied position, I concluded that this position
# must be somewhere adjacent to some sensors ranges (otherwise it would be
# detected by those sensors; and if they were farther, there would be more
# than just single such possible position).
#
#   .....B####S#####....####S###B.....
#   .....B####S#####.####S###B........
#
# Therefore the difference here is that instead of X ranges for a specific
# Y position, we produce a list of candidates (all positions that are just
# next to the sensors ranges, marked x on the illustration below).
#
#   ...............................
#   ......x........................
#   .....x#x.......................
#   ....x###x......................
#   ...x##S#Bx.....................
#   ....x###x......................
#   .....x#x.......................
#   ......x........................
#   ...............................
#
# Then we check the distance of each candidate to every sonar we know about.
# If it is less distant than the closest beacon of any sonar, then this is not
# a valid candidate (it would have been detected instead). When we find such
# a point that is not in range of any sonar, then this is our solution to this
# part. All we need then is to calculate its coordinates (xc, yc) according
# to the given formula and return the result as an answer.
# It is probably far from perfect, but it finds the solution in a finite time
# (under 5 minutes, so far from perfect, but acceptable right now).
#
# Edit: I came up with an idea that the set of candidates is very large
# and it is very ineffective to store it in memory for processing later.
# Instead can verify the each of the candidates just after calculating
# its probable position (so we just move the inner verification loop).
# This reduces the calculation time from around 5 minutes to about 1 minute.
#
# Edit: Extending the previous idea, I realized that if there are so many
# candidates, calculating every time the distance in the inner loop is another
# bottleneck. Hence calculating the sensors ranges only once on the beginning
# does reduce the calculations time from about 1 minute to around 40 seconds
# (after all, it turned out it was the only place where the beacons were used).
#

INPUT_FILE = 'input.txt'

MIN = 0
MAX = 4000000


def main():
    with open(INPUT_FILE, 'r') as file:
        sensors = [tuple(map(int, line.split(', ')))
                   for line in file.read()
                                   .replace('Sensor at x=', '')
                                   .replace('closest beacon is at x=', '')
                                   .replace('y=', '')
                                   .replace(':', ',')
                                   .strip()
                                   .split('\n')]
        sensors = [(x1, y1, abs(x1 - x2) + abs(y1 - y2))
                   for x1, y1, x2, y2 in sensors]

    found = False

    for sx, sy, srange in sensors:
        target_distance = srange + 1

        for dx in range(0, target_distance + 1):
            dy = target_distance - dx

            for xc, yc in ((sx + dx, sy + dy),
                           (sx - dx, sy + dy),
                           (sx + dx, sy - dy),
                           (sx - dx, sy - dy)):
                if MIN <= xc <= MAX and MIN <= yc <= MAX:
                    for nx, ny, nrange in sensors:
                        candidate_distance = abs(nx - xc) + abs(ny - yc)

                        if candidate_distance <= nrange:
                            break  # this cannot be the right position
                    else:
                        found = True
                        break  # we found it!
            if found:
                break
        if found:
            break

    tuning_frequency = xc * MAX + yc
    print(tuning_frequency)


if __name__ == '__main__':
    main()
