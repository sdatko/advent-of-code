#!/usr/bin/env python3
#
# Task:
# You still can't quite make out the details in the image.
# Maybe you just didn't enhance it enough.
# If you enhance the starting input image in the above example a total
# of 50 times, 3351 pixels are lit in the final output image.
# Start again with the original input image and apply the image enhancement
# algorithm 50 times. How many pixels are lit in the resulting image?
#
# Solution:
# The only difference here was to change the number of step in the loop.
# It produces the result quickly enough for no further work here needed.
#

INPUT_FILE = 'input.txt'


def pad_with_background(image, background='.', size=1):
    width = len(image[0])
    new_image = []

    for _ in range(size):
        new_image.append([background] * (width + 2 * size))

    for row in image:
        new_image.append([background] * size + row + [background] * size)

    for _ in range(size):
        new_image.append([background] * (width + 2 * size))

    return new_image


def enhance(image, algorithm, background='.'):
    width = len(image[0])
    height = len(image)
    new_image = [[background] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            index = ''

            for ny in [y - 1, y, y + 1]:
                for nx in [x - 1, x, x + 1]:
                    if nx < 0 or ny < 0 or nx >= width or ny >= height:
                        if background == '#':
                            index += '1'
                        else:
                            index += '0'
                    elif image[ny][nx] == '#':
                        index += '1'
                    else:
                        index += '0'

            new_image[y][x] = algorithm[int(index, 2)]

    return new_image


def main():
    with open(INPUT_FILE, 'r') as file:
        algorithm, image = file.read().strip().split('\n\n')
        image = [list(row) for row in image.split('\n')]

    background_image = [['.']]

    for step in range(50):
        image = pad_with_background(image, background_image[0][0])
        image = enhance(image, algorithm, background_image[0][0])
        background_image = enhance(background_image, algorithm,
                                   background_image[0][0])

    print(''.join([''.join(row) for row in image]).count('#'))


if __name__ == '__main__':
    main()
