#!/usr/bin/env python3
#
# --- Day 20: Jurassic Jigsaw / Part Two ---
#
# Now, you're ready to check the image for sea monsters.
#
# The borders of each tile are not part of the actual image;
# start by removing them.
#
# In the example above, the tiles become:
#
#   .#.#..#. ##...#.# #..#####
#   ###....# .#....#. .#......
#   ##.##.## #.#.#..# #####...
#   ###.#### #...#.## ###.#..#
#   ##.#.... #.##.### #...#.##
#   ...##### ###.#... .#####.#
#   ....#..# ...##..# .#.###..
#   .####... #..#.... .#......
#
#   #..#.##. .#..###. #.##....
#   #.####.. #.####.# .#.###..
#   ###.#.#. ..#.#### ##.#..##
#   #.####.. ..##..## ######.#
#   ##..##.# ...#...# .#.#.#..
#   ...#..#. .#.#.##. .###.###
#   .#.#.... #.##.#.. .###.##.
#   ###.#... #..#.##. ######..
#
#   .#.#.### .##.##.# ..#.##..
#   .####.## #.#...## #.#..#.#
#   ..#.#..# ..#.#.#. ####.###
#   #..####. ..#.#.#. ###.###.
#   #####..# ####...# ##....##
#   #.##..#. .#...#.. ####...#
#   .#.###.. ##..##.. ####.##.
#   ...###.. .##...#. ..#..###
#
# Remove the gaps to form the actual image:
#
#   .#.#..#.##...#.##..#####
#   ###....#.#....#..#......
#   ##.##.###.#.#..######...
#   ###.#####...#.#####.#..#
#   ##.#....#.##.####...#.##
#   ...########.#....#####.#
#   ....#..#...##..#.#.###..
#   .####...#..#.....#......
#   #..#.##..#..###.#.##....
#   #.####..#.####.#.#.###..
#   ###.#.#...#.######.#..##
#   #.####....##..########.#
#   ##..##.#...#...#.#.#.#..
#   ...#..#..#.#.##..###.###
#   .#.#....#.##.#...###.##.
#   ###.#...#..#.##.######..
#   .#.#.###.##.##.#..#.##..
#   .####.###.#...###.#..#.#
#   ..#.#..#..#.#.#.####.###
#   #..####...#.#.#.###.###.
#   #####..#####...###....##
#   #.##..#..#...#..####...#
#   .#.###..##..##..####.##.
#   ...###...##...#...#..###
#
# Now, you're ready to search for sea monsters! Because your image
# is monochrome, a sea monster will look like this:
#
#                     #
#   #    ##    ##    ###
#    #  #  #  #  #  #
#
# When looking for this pattern in the image, the spaces can be anything;
# only the # need to match. Also, you might need to rotate or flip your image
# before it's oriented correctly to find sea monsters. In the above image,
# after flipping and rotating it to the appropriate orientation, there are
# two sea monsters (marked with O):
#
#   .####...#####..#...###..
#   #####..#..#.#.####..#.#.
#   .#.#...#.###...#.##.O#..
#   #.O.##.OO#.#.OO.##.OOO##
#   ..#O.#O#.O##O..O.#O##.##
#   ...#.#..##.##...#..#..##
#   #.##.#..#.#..#..##.#.#..
#   .###.##.....#...###.#...
#   #.####.#.#....##.#..#.#.
#   ##...#..#....#..#...####
#   ..#.##...###..#.#####..#
#   ....#.##.#.#####....#...
#   ..##.##.###.....#.##..#.
#   #...#...###..####....##.
#   .#.##...#.##.#.#.###...#
#   #.###.#..####...##..#...
#   #.###...#.##...#.##O###.
#   .O##.#OO.###OO##..OOO##.
#   ..O#.O..O..O.#O##O##.###
#   #.#..##.########..#..##.
#   #.#####..#.#...##..#....
#   #....##..#.#########..##
#   #...#.....#..##...###.##
#   #..###....##.#...##.##.#
#
# Determine how rough the waters are in the sea monsters' habitat by counting
# the number of # that are not part of a sea monster. In the above example,
# the habitat's water roughness is 273.
#
# How many # are not part of a sea monster?
#
#
# --- Solution ---
#
# The difference here is that we need to assemble the actual image and count
# occurrences of given pattern on the assembled image (including that it can
# also be rotated like all the tiles previously). The task assumes that final
# image would be a square (see part 1 description), so we allocate an array
# of size N equal to the square root of total number of all available tiles
# for tracking the positions of finally arranged tiles after rotations. Then
# we take any corner previously found and assembly it with its two neighbors.
# We get the relative positions of the corner tile and the neighbors to detect
# their orientation and then we rotate all these tiles until they would fit
# the top-left corner of the image. At this point we can remove from the list
# of matched tiles the ones we already arranged. Then, we can fill the rest
# of arrangements array – for the already arranged tiles, we can detect their
# neighbors, then transform them to align properly and save their location
# in the arrangements array; then we do the same for the newly arranged tiles
# until all tiles are arranged.
#
#                   ##???      #####      #####      #####      #####
#    #              #????      #????      #####      #####      #####
#   ##  ->  ##  ->  ?????  ->  ?????  ->  ?????  ->  #####  ->  #####
#           #       ?????      ?????      ?????      ?????      #####
#                   ?????      ?????      ?????      ?????      #####
#
# Having the tiles properly oriented and knowing their arrangement, we proceed
# to assembling the image by joining the multiple tiles into a single 2D array.
# After than, we can proceed to detecting the sea monsters, using a sliding
# window of size 3 x 20 and a mask visible below to detect that all necessary
# characters are on the demanded positions.
#
#    |01234567890123456789|
#   -+--------------------+-
#   0|                  # |0
#   1|#    ##    ##    ###|1
#   2| #  #  #  #  #  #   |2
#   -+--------------------+-
#    |01234567890123456789|
#
# We perform the detection of every possible rotation & flip of the assembled
# image until we find the orientation where any sea monsters were found.
# Finally, for an answer, we count the number of # characters in the assembled
# image and we subtract the number of sea monsters multiplied by the number
# of characters each sea monster is built of.
#

INPUT_FILE = 'input.txt'

HASHES_PER_MONSTER = 15


def get_col(matrix, index):
    return [row[index] for row in matrix]


def get_row(matrix, index):
    return matrix[index]


def flip_h(matrix: tuple[tuple[str]]) -> tuple[tuple[str]]:
    return tuple(tuple(reversed(row)) for row in matrix)


def flip_v(matrix: tuple[tuple[str]]) -> tuple[tuple[str]]:
    return tuple(row for row in reversed(matrix))


def identity(matrix: tuple[tuple[str]]) -> tuple[tuple[str]]:
    return matrix


def rotate_l(matrix: tuple[tuple[str]]) -> tuple[tuple[str]]:
    return tuple(zip(*matrix))[::-1]


def rotate_ll(matrix: tuple[tuple[str]]) -> tuple[tuple[str]]:
    return rotate_l(rotate_l(matrix))


def rotate_lll(matrix: tuple[tuple[str]]) -> tuple[tuple[str]]:
    return rotate_r(matrix)


def rotate_r(matrix: tuple[tuple[str]]) -> tuple[tuple[str]]:
    return tuple(zip(*matrix[::-1]))


def rotate_rr(matrix: tuple[tuple[str]]) -> tuple[tuple[str]]:
    return rotate_r(rotate_r(matrix))


def rotate_rrr(matrix: tuple[tuple[str]]) -> tuple[tuple[str]]:
    return rotate_l(matrix)


def matches(tile1: tuple[tuple[str]], tile2: tuple[tuple[str]]) -> bool:
    for transform1 in (identity, flip_v, flip_h):
        for transform2 in (identity, rotate_r, rotate_rr, rotate_rrr):
            transformed_tile2 = transform2(transform1(tile2))

            if any([get_col(tile1, -1) == get_col(transformed_tile2, 0),
                    get_col(tile1, 0) == get_col(transformed_tile2, -1),
                    get_row(tile1, 0) == get_row(transformed_tile2, -1),
                    get_row(tile1, -1) == get_row(transformed_tile2, 0)]):
                return True

    return False


def align(tile1: tuple[tuple[str]], tile2: tuple[tuple[str]]) -> tuple[int]:
    for transform1 in (identity, flip_v, flip_h):
        for transform2 in (identity, rotate_r, rotate_rr, rotate_rrr):
            transformed_tile2 = transform2(transform1(tile2))

            if get_col(tile1, -1) == get_col(transformed_tile2, 0):
                return 1, 0, transformed_tile2

            if get_col(tile1, 0) == get_col(transformed_tile2, -1):
                return -1, 0, transformed_tile2

            if get_row(tile1, 0) == get_row(transformed_tile2, -1):
                return 0, -1, transformed_tile2

            if get_row(tile1, -1) == get_row(transformed_tile2, 0):
                return 0, 1, transformed_tile2

    return 0, 0, tile2  # cannot align


def assemble(tiles: dict[tuple[tuple[str]]],
             arrangement: list[list[int]]) -> tuple[tuple[str]]:
    image = []

    for y in range(len(arrangement)):
        tiles_in_row = [tiles[ID] for ID in arrangement[y]]

        for rows in tuple(zip(*tiles_in_row))[1:-1]:
            image_row = []

            for row in rows:
                image_row.extend(row[1:-1])

            image.append(tuple(image_row))

    return tuple(image)


def is_sea_monster(matrix: tuple[tuple[str]]) -> bool:
    characters = (matrix[0][18], matrix[1][0], matrix[1][5],
                  matrix[1][6], matrix[1][11], matrix[1][12],
                  matrix[1][17], matrix[1][18], matrix[1][19],
                  matrix[2][1], matrix[2][4], matrix[2][7],
                  matrix[2][10], matrix[2][13], matrix[2][16])

    return all(character == '#' for character in characters)


def detect_sea_monsters(image: tuple[tuple[str]]) -> bool:
    height = len(image)
    width = len(image[0])
    count = 0

    for y in range(height - 3):
        for x in range(width - 20):
            characters = (image[y + 0][x + 18],
                          image[y + 1][x + 0],
                          image[y + 1][x + 5],
                          image[y + 1][x + 6],
                          image[y + 1][x + 11],
                          image[y + 1][x + 12],
                          image[y + 1][x + 17],
                          image[y + 1][x + 18],
                          image[y + 1][x + 19],
                          image[y + 2][x + 1],
                          image[y + 2][x + 4],
                          image[y + 2][x + 7],
                          image[y + 2][x + 10],
                          image[y + 2][x + 13],
                          image[y + 2][x + 16])

            if all(character == '#' for character in characters):
                count += 1

    return count


def main():
    with open(INPUT_FILE, 'r') as file:
        tiles = [tile.replace('Tile ', '').split(':\n')
                 for tile in file.read().strip().split('\n\n')]
        tiles = {int(ID): tuple(map(tuple, image.split('\n')))
                 for ID, image in tiles}

    matched_tiles = {key: [] for key in tiles.keys()}
    unmatched_tiles = tiles.copy()

    for ID1, tile1 in tiles.items():
        del unmatched_tiles[ID1]

        for ID2, tile2 in unmatched_tiles.items():
            if matches(tile1, tile2):
                matched_tiles[ID1].append(ID2)
                matched_tiles[ID2].append(ID1)

    corner_tiles = [key
                    for key, value in matched_tiles.items()
                    if len(value) == 2]

    assert len(corner_tiles) == 4

    N = int(len(tiles) ** 0.5)  # image size
    arranged = [[None] * N for _ in range(N)]

    # Get corner tile and its neighbors
    corner_tile = corner_tiles[0]
    neighbor1, neighbor2 = matched_tiles[corner_tile]

    dx1, dy1, tiles[neighbor1] = align(tiles[corner_tile], tiles[neighbor1])
    dx2, dy2, tiles[neighbor2] = align(tiles[corner_tile], tiles[neighbor2])

    dir1 = complex(dx1, -dy1)  # minus Y here, because in align() we return
    dir2 = complex(dx2, -dy2)  # the arrangement in IT-like coordinate system
    desired_orientation = [complex(1, 0), complex(0, -1)]

    # Rotate clockwise until the arrangement fits top-left corner of image
    while dir1 not in desired_orientation or dir2 not in desired_orientation:
        dir1 *= complex(0, -1)
        dir2 *= complex(0, -1)

        tiles[corner_tile] = rotate_r(tiles[corner_tile])
        tiles[neighbor1] = rotate_r(tiles[neighbor1])
        tiles[neighbor2] = rotate_r(tiles[neighbor2])

    # Set the top-left corner of image
    arranged[0][0] = corner_tile

    if dir1 == complex(1, 0):  # first neighbor is on the right of the corner
        arranged[0][1] = neighbor1
        arranged[1][0] = neighbor2
    else:  # first neighbor is below the corner
        arranged[0][1] = neighbor2
        arranged[1][0] = neighbor1

    # Remove already arranged tiles from matched list (for easier future...)
    matched_tiles[corner_tile].remove(neighbor1)
    matched_tiles[corner_tile].remove(neighbor2)
    matched_tiles[neighbor1].remove(corner_tile)
    matched_tiles[neighbor2].remove(corner_tile)

    # Arrange rest of image
    for y in range(N):
        for x in range(N):
            reference_tile = arranged[y][x]

            for neighbor in matched_tiles[reference_tile].copy():
                dx, dy, tiles[neighbor] = align(tiles[reference_tile],
                                                tiles[neighbor])

                arranged[y + dy][x + dx] = neighbor
                matched_tiles[reference_tile].remove(neighbor)
                matched_tiles[neighbor].remove(reference_tile)

    # Assemble image
    image = assemble(tiles, arranged)

    # Detect sea monsters!
    for transform1 in (identity, flip_v, flip_h):
        for transform2 in (identity, rotate_r, rotate_rr, rotate_rrr):
            transformed_image = transform2(transform1(image))

            count = detect_sea_monsters(transformed_image)

            if count:
                break
        if count:
            break

    # Calculate the answer
    hashes = ''.join(''.join(row) for row in transformed_image).count('#')
    answer = hashes - count * HASHES_PER_MONSTER

    print(answer)


if __name__ == '__main__':
    main()
