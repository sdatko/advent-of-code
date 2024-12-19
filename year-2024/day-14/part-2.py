#!/usr/bin/env python3
#
# --- Day 14: Restroom Redoubt / Part Two ---
#
# During the bathroom break, someone notices that these robots seem awfully
# similar to ones built and used at the North Pole. If they're the same type
# of robots, they should have a hard-coded Easter egg: very rarely, most of
# the robots should arrange themselves into a picture of a Christmas tree.
#
# What is the fewest number of seconds that must elapse for the robots
# to display the Easter egg?
#
#
# --- Solution ---
#
# The difference in this part is that we need to conduct the calculations
# as long as after some time the robots locations form a specific shape.
# However, the puzzle does not describe any details about the shape, except
# that it is a Christmas tree, so the only obvious approach seems to be
# printing and browsing the results as long as we find the expected shape.
# The portable pixmap format (PPM) works here quite well and do not require
# any imports – the results can be then quickly analyzed with files browser
# or images browser (such as `feh`).
#
# However, there can be a few important observations made:
# – When browsing the results, one can notice that occasionally there are
#   repeatably appearing patterns of horizontal and vertical lines in outputs.
#   For my data, the vertical lines appeared first on 69th frame, then 170th,
#   then 271st and so on, while the horizontal lines appeared on 12th frame,
#   115th, 218th and so on). The repetition periods corresponds with the floor
#   dimensions that are pairwise prime numbers, which may suggest the usage
#   of the Chinese remainder theorem. Putting the equations into solver:
#     69 = x mod 101
#     12 = x mod 103
#   we get a formula:
#     12 = (69 + t * 101) mod 103
#   which is first satisfied for t = 80 and hence x = 69 + 80 * 101 = 8149,
#   that is apparently a correct answer.
# – Surprisingly, the correct answer also appears when a stop condition
#   of each robot being on unique position is used, although this may be
#   an input-specific case, as there is no particular reason (given in puzzle)
#   why two robots should not share the same position in the Easter Egg image.
# – When the Easter Egg image is produced, there is a lot of robots next to
#   each other, so this results in sequences of pixels of low entropy that can
#   be efficiently compressed via algorithms involving e.g. Huffman-encoding,
#   such as zlib. Hence, the output image, converted to PNG format, has
#   the smallest size of in collection:
#     [sdatko@altair day-14]$ ls -lh --sort=size *.png | tail -n 1
#     -rw-r--r-- 1 sdatko sdatko 619 Dec 14 22:16 output_008149.ppm.png
# – The stop condition can be defined as finding a pattern of long horizontal
#   line in the generated image (although depending on the input there exist
#   a possibility for some horizontal lines to appear occasionally in output,
#   the long line is very unlikely to appear except for the Easter Egg case).
# – One other idea it to look for symmetry in all possible cases and picking
#   the one where the highest vertical symmetry score is reached.
#

INPUT_FILE = 'input.txt'

MAX_X = 101
MAX_Y = 103


def save(image, time):
    # This is PBM variant of the PPM format (using binary values)
    # https://en.wikipedia.org/wiki/Netpbm#File_formats
    with open(f'output_{time:06d}.ppm', 'w') as file:
        file.write(f'P1 {MAX_X} {MAX_Y}\n')  # header
        for row in image:
            file.write(' '.join(map(str, row)) + '\n')


def main():
    with open(INPUT_FILE, 'r') as file:
        robots = tuple(tuple(map(int, robot.split(',')))
                       for robot in file.read().strip()
                                               .replace('p=', '')
                                               .replace('v=', '')
                                               .replace(' ', ',')
                                               .split())

    image_empty = [[0 for x in range(MAX_X)] for y in range(MAX_Y)]

    for time in range(MAX_X * MAX_Y):
        image = [row.copy() for row in image_empty]
        locations = set()

        for robot in robots:
            x, y = robot[0:2]
            Vx, Vy = robot[2:4]

            x = (x + Vx * time) % MAX_X
            y = (y + Vy * time) % MAX_Y

            image[y][x] = 1
            locations.add((x, y))

        # Save the image for browsing
        # save(image, time)

        # Stop condition based on unique locations
        if len(locations) == len(robots):
            # save(image, time)
            break

        # Stop condition based on pattern finding
        # pattern = ', '.join('1' * 10)
        # if any(str(row).find(pattern) >= 0 for row in image):
        #     break

    print(time)


if __name__ == '__main__':
    main()
