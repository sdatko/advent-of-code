#!/usr/bin/env python3
#
# --- Day 20: Jurassic Jigsaw ---
#
# The high-speed train leaves the forest and quickly carries you south.
# You can even see a desert in the distance! Since you have some spare time,
# you might as well see if there was anything interesting in the image
# the Mythical Information Bureau satellite captured.
#
# After decoding the satellite messages, you discover that the data actually
# contains many small images created by the satellite's camera array.
# The camera array consists of many cameras; rather than produce a single
# square image, they produce many smaller square image tiles that need
# to be reassembled back into a single image.
#
# Each camera in the camera array returns a single monochrome image tile
# with a random unique ID number. The tiles (your puzzle input) arrived
# in a random order.
#
# Worse yet, the camera array appears to be malfunctioning: each image
# tile has been rotated and flipped to a random orientation. Your first
# task is to reassemble the original image by orienting the tiles so they
# fit together.
#
# To show how the tiles should be reassembled, each tile's image data
# includes a border that should line up exactly with its adjacent tiles.
# All tiles have this border, and the border lines up exactly when the tiles
# are both oriented correctly. Tiles at the edge of the image also have this
# border, but the outermost edges won't line up with any other tiles.
#
# For example, suppose you have the following nine tiles:
#
#   Tile 2311:
#   ..##.#..#.
#   ##..#.....
#   #...##..#.
#   ####.#...#
#   ##.##.###.
#   ##...#.###
#   .#.#.#..##
#   ..#....#..
#   ###...#.#.
#   ..###..###
#
#   Tile 1951:
#   #.##...##.
#   #.####...#
#   .....#..##
#   #...######
#   .##.#....#
#   .###.#####
#   ###.##.##.
#   .###....#.
#   ..#.#..#.#
#   #...##.#..
#
#   Tile 1171:
#   ####...##.
#   #..##.#..#
#   ##.#..#.#.
#   .###.####.
#   ..###.####
#   .##....##.
#   .#...####.
#   #.##.####.
#   ####..#...
#   .....##...
#
#   Tile 1427:
#   ###.##.#..
#   .#..#.##..
#   .#.##.#..#
#   #.#.#.##.#
#   ....#...##
#   ...##..##.
#   ...#.#####
#   .#.####.#.
#   ..#..###.#
#   ..##.#..#.
#
#   Tile 1489:
#   ##.#.#....
#   ..##...#..
#   .##..##...
#   ..#...#...
#   #####...#.
#   #..#.#.#.#
#   ...#.#.#..
#   ##.#...##.
#   ..##.##.##
#   ###.##.#..
#
#   Tile 2473:
#   #....####.
#   #..#.##...
#   #.##..#...
#   ######.#.#
#   .#...#.#.#
#   .#########
#   .###.#..#.
#   ########.#
#   ##...##.#.
#   ..###.#.#.
#
#   Tile 2971:
#   ..#.#....#
#   #...###...
#   #.#.###...
#   ##.##..#..
#   .#####..##
#   .#..####.#
#   #..#.#..#.
#   ..####.###
#   ..#.#.###.
#   ...#.#.#.#
#
#   Tile 2729:
#   ...#.#.#.#
#   ####.#....
#   ..#.#.....
#   ....#..#.#
#   .##..##.#.
#   .#.####...
#   ####.#.#..
#   ##.####...
#   ##..#.##..
#   #.##...##.
#
#   Tile 3079:
#   #.#.#####.
#   .#..######
#   ..#.......
#   ######....
#   ####.#..#.
#   .#...#.##.
#   #.#####.##
#   ..#.###...
#   ..#.......
#   ..#.###...
#
# By rotating, flipping, and rearranging them, you can find a square
# arrangement that causes all adjacent borders to line up:
#
#   #...##.#.. ..###..### #.#.#####.
#   ..#.#..#.# ###...#.#. .#..######
#   .###....#. ..#....#.. ..#.......
#   ###.##.##. .#.#.#..## ######....
#   .###.##### ##...#.### ####.#..#.
#   .##.#....# ##.##.###. .#...#.##.
#   #...###### ####.#...# #.#####.##
#   .....#..## #...##..#. ..#.###...
#   #.####...# ##..#..... ..#.......
#   #.##...##. ..##.#..#. ..#.###...
#
#   #.##...##. ..##.#..#. ..#.###...
#   ##..#.##.. ..#..###.# ##.##....#
#   ##.####... .#.####.#. ..#.###..#
#   ####.#.#.. ...#.##### ###.#..###
#   .#.####... ...##..##. .######.##
#   .##..##.#. ....#...## #.#.#.#...
#   ....#..#.# #.#.#.##.# #.###.###.
#   ..#.#..... .#.##.#..# #.###.##..
#   ####.#.... .#..#.##.. .######...
#   ...#.#.#.# ###.##.#.. .##...####
#
#   ...#.#.#.# ###.##.#.. .##...####
#   ..#.#.###. ..##.##.## #..#.##..#
#   ..####.### ##.#...##. .#.#..#.##
#   #..#.#..#. ...#.#.#.. .####.###.
#   .#..####.# #..#.#.#.# ####.###..
#   .#####..## #####...#. .##....##.
#   ##.##..#.. ..#...#... .####...#.
#   #.#.###... .##..##... .####.##.#
#   #...###... ..##...#.. ...#..####
#   ..#.#....# ##.#.#.... ...##.....
#
# For reference, the IDs of the above tiles are:
#
#   1951    2311    3079
#   2729    1427    2473
#   2971    1489    1171
#
# To check that you've assembled the image correctly, multiply the IDs
# of the four corner tiles together. If you do this with the assembled
# tiles from the example above, you get 1951 * 3079 * 2971 * 1171
# = 20899048083289.
#
# Assemble the tiles into an image. What do you get if you multiply
# together the IDs of the four corner tiles?
#
#
# --- Solution ---
#
# We start by reading the input file into a dictionary of tiles, by splitting
# first over two newline characters, then each tile over newlines and mapping
# each line to tuple and keeping the tile number as key, so in the end we get
# 2D tuple of characters for each dictionary key. Then we define a bunch of
# helper function to transform the 2D tuples – including flipping the image
# vertically and horizontally, as well as rotating by 90, 180 and 270 degrees.
# Then in a loop we can take every tile and compare it with the remaining ones
# to find the matching neighbors; for each pair, we try different arrangements
# (transformations applied) of the second tile to see if any two sides matches
# – there are four possible cases to check:
#      [ ]         [ ]         [2]         [ ]
#   [ ][1][2]   [ ][2][1]   [ ][1][ ]   [ ][2][ ]
#      [ ]         [ ]         [ ]         [1]
# When all tiles were checked and all their possible neighbors were determined,
# the answer for this part can be found quickly by determining all corner tiles
# – that would be the ones that have exactly two neighbors. So, after filtering
# and multiplying IDs of such tiles, this part is done.
#

INPUT_FILE = 'input.txt'


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

    answer = 1
    for ID in corner_tiles:
        answer *= ID

    print(answer)


if __name__ == '__main__':
    main()
