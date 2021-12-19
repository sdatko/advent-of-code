#!/usr/bin/env python3
#
# Task:
# Sometimes, it's a good idea to appreciate just how big the ocean is.
# Using the Manhattan distance, how far apart do the scanners get?
# In the above example, scanners 2 (1105,-1205,1229) and 3 (-92,-2380,-20)
# are the largest Manhattan distance apart. In total, they are 1197 + 1175
# + 1249 = 3621 units apart.
# What is the largest Manhattan distance between any two scanners?
#
# Solution:
# To find the scanners positions, relative to our chosen origin point, after
# we found the proper rotation and translation vector, we just need to sum
# the coordinates of the beacon from the known set we used and the inverse of
# the matched beacon position (because it is given as a relative to the scanner
# position: S -------> B; if we invert it, we have a vector pointing to the
# location of scanner: S <------- B). Finally we just calculate the sums of
# absolute differences on coordinates between all scanners positions we found
# and as an answer we print the biggest one.
#

INPUT_FILE = 'input.txt'


def sin(angle):
    angle %= 360
    if angle == 0 or angle == 180:
        return 0
    elif angle == 90:
        return 1
    elif angle == 270:
        return -1
    raise ValueError('Only the multiples of the right angle are supported.')


def cos(angle):
    return sin(angle + 90)


def rotation_x(angle, vec):
    return [
        vec[0],
        cos(angle) * vec[1] + -sin(angle) * vec[2],
        sin(angle) * vec[1] + cos(angle) * vec[2],
    ]


def rotation_y(angle, vec):
    return [
        cos(angle) * vec[0] + sin(angle) * vec[2],
        vec[1],
        -sin(angle) * vec[0] + cos(angle) * vec[2],
    ]


def rotation_z(angle, vec):
    return [
        cos(angle) * vec[0] + -sin(angle) * vec[1],
        sin(angle) * vec[0] + cos(angle) * vec[1],
        vec[2],
    ]


def rotation_xyz(angle_x, angle_y, angle_z, vec):
    return rotation_z(angle_z, rotation_y(angle_y, rotation_x(angle_x, vec)))


def abs(value):
    if value >= 0:
        return value
    else:
        return -value


def sign(value):
    if value >= 0:
        return 1
    elif value < 0:
        return -1


def main():
    with open(INPUT_FILE, 'r') as file:
        scanners = file.read().strip().split('\n\n')

    for i, scanner in enumerate(scanners):
        scanners[i] = [tuple(map(int, line.split(',')))
                       for line in scanner.split('\n')[1:]]

    rotations = set()
    transformations = set()

    for angle1 in [0, 90, 180, 270]:
        for angle2 in [0, 90, 180, 270]:
            for angle3 in [0, 90, 180, 270]:
                vec = rotation_xyz(angle1, angle2, angle3, [1, 2, 3])
                rotations.add(tuple(vec))

    for transformation in rotations:
        indexes = tuple([abs(component) - 1 for component in transformation])
        signs = tuple([sign(component) for component in transformation])
        transformations.add((indexes, signs))

    known = set(scanners.pop(0))  # first scanner is our origin point (0, 0, 0)
    scanner_positions = [(0, 0, 0)]

    while scanners:
        matched = False
        for scanner in scanners:
            for transformation in transformations:
                indexes, signs = transformation
                nx, ny, nz = indexes
                s1, s2, s3 = signs
                rotated = [(s1 * beacon[nx], s2 * beacon[ny], s3 * beacon[nz])
                           for beacon in scanner]

                for reading in known:
                    for beacon in rotated:
                        dx, dy, dz = [b_i - r_i
                                      for b_i, r_i in zip(beacon, reading)]

                        translated = set([(x - dx, y - dy, z - dz)
                                          for candidate in rotated
                                          for x, y, z in [candidate]])

                        common_points = known.intersection(translated)

                        if len(common_points) >= 12:
                            scanner_position = tuple(
                                [r_i + -b_i
                                 for b_i, r_i in zip(beacon, reading)]
                            )
                            scanner_positions.append(scanner_position)

                            known = known.union(translated)
                            matched = True
                            break

                    if matched:
                        break

                if matched:
                    break

            if matched:
                break

        if matched:
            scanners.remove(scanner)
        else:
            print('Went through all, no match – something is wrong!')
            break

    distances = []
    for index, scanner1 in enumerate(scanner_positions):
        for scanner2 in scanner_positions[index + 1:]:
            L1 = sum([abs(s1_i - s2_i)
                      for s1_i, s2_i in zip(scanner1, scanner2)])
            distances.append(L1)

    print(max(distances))


if __name__ == '__main__':
    main()
