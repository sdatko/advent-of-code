#!/usr/bin/env python3
#
# --- Day 11: Plutonian Pebbles / Part Two ---
#
# The Historians sure are taking a long time.
# To be fair, the infinite corridors are very large.
#
# How many stones would you have after blinking a total of 75 times?
#
#
# --- Solution ---
#
# The difference here is that we need to perform more iterations – however,
# the number of stones grows exponentially, so quickly it would require
# too much resources to store the elements and process the efficiently.
# However, in the task we only care about the count of the stones, not about
# their relative placement. Hence, instead of processing the list of individual
# stones, it is better utilize a dictionary containing counts of each stone.
# After all, if there is a single stone with number 1, it will become a stone
# number 2024; if there are two stones with numbers (1, 1), they will become
# (2024, 2024) – in other words, {1: 2} becomes {2024: 2}. The main algorithm
# and rest of the processing remain the same. Finally, as an answer we return
# the sum of counts from the dictionary.
#

INPUT_FILE = 'input.txt'

BLINKS = 75


def main():
    with open(INPUT_FILE, 'r') as file:
        stones = list(map(int, file.read().strip().split()))

    stones = {
        stone: stones.count(stone)
        for stone in stones
    }

    for blink in range(BLINKS):
        new_stones = {}

        for stone, count in stones.items():
            if stone == 0:
                new_stone = 1

                if new_stone not in new_stones:
                    new_stones[new_stone] = 0

                new_stones[new_stone] += count

            elif len(str(stone)) % 2 == 0:
                stone = str(stone)
                digits = len(stone)
                new_stone1 = int(stone[:digits // 2])
                new_stone2 = int(stone[digits // 2:])

                if new_stone1 not in new_stones:
                    new_stones[new_stone1] = 0
                if new_stone2 not in new_stones:
                    new_stones[new_stone2] = 0

                new_stones[new_stone1] += count
                new_stones[new_stone2] += count

            else:
                new_stone = stone * 2024

                if new_stone not in new_stones:
                    new_stones[new_stone] = 0

                new_stones[new_stone] += count

        stones = new_stones

    print(sum(stones.values()))


if __name__ == '__main__':
    main()
