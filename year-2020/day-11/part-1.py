#!/usr/bin/env python3
#
# --- Day 11: Seating System ---
#
# Your plane lands with plenty of time to spare. The final leg of your journey
# is a ferry that goes directly to the tropical island where you can finally
# start your vacation. As you reach the waiting area to board the ferry,
# you realize you're so early, nobody else has even arrived yet!
#
# By modeling the process people use to choose (or abandon) their seat
# in the waiting area, you're pretty sure you can predict the best place
# to sit. You make a quick map of the seat layout (your puzzle input).
#
# The seat layout fits neatly on a grid. Each position is either floor (.),
# an empty seat (L), or an occupied seat (#). For example, the initial seat
# layout might look like this:
#
#   L.LL.LL.LL
#   LLLLLLL.LL
#   L.L.L..L..
#   LLLL.LL.LL
#   L.LL.LL.LL
#   L.LLLLL.LL
#   ..L.L.....
#   LLLLLLLLLL
#   L.LLLLLL.L
#   L.LLLLL.LL
#
# Now, you just need to model the people who will be arriving shortly.
# Fortunately, people are entirely predictable and always follow a simple
# set of rules. All decisions are based on the number of occupied seats
# adjacent to a given seat (one of the eight positions immediately up,
# down, left, right, or diagonal from the seat). The following rules are
# applied to every seat simultaneously:
#
# – If a seat is empty (L) and there are no occupied seats adjacent to it,
#   the seat becomes occupied.
# – If a seat is occupied (#) and four or more seats adjacent to it are
#   also occupied, the seat becomes empty.
# – Otherwise, the seat's state does not change.
#
# Floor (.) never changes; seats don't move, and nobody sits on the floor.
#
# After one round of these rules, every seat
# in the example layout becomes occupied:
#
#   #.##.##.##
#   #######.##
#   #.#.#..#..
#   ####.##.##
#   #.##.##.##
#   #.#####.##
#   ..#.#.....
#   ##########
#   #.######.#
#   #.#####.##
#
# After a second round, the seats with four or more
# occupied adjacent seats become empty again:
#
#   #.LL.L#.##
#   #LLLLLL.L#
#   L.L.L..L..
#   #LLL.LL.L#
#   #.LL.LL.LL
#   #.LLLL#.##
#   ..L.L.....
#   #LLLLLLLL#
#   #.LLLLLL.L
#   #.#LLLL.##
#
# This process continues for three more rounds:
#
#   #.##.L#.##
#   #L###LL.L#
#   L.#.#..#..
#   #L##.##.L#
#   #.##.LL.LL
#   #.###L#.##
#   ..#.#.....
#   #L######L#
#   #.LL###L.L
#   #.#L###.##
#
#   #.#L.L#.##
#   #LLL#LL.L#
#   L.L.L..#..
#   #LLL.##.L#
#   #.LL.LL.LL
#   #.LL#L#.##
#   ..L.L.....
#   #L#LLLL#L#
#   #.LLLLLL.L
#   #.#L#L#.##
#
#   #.#L.L#.##
#   #LLL#LL.L#
#   L.#.L..#..
#   #L##.##.L#
#   #.#L.LL.LL
#   #.#L#L#.##
#   ..L.L.....
#   #L#L##L#L#
#   #.LLLLLL.L
#   #.#L#L#.##
#
# At this point, something interesting happens: the chaos stabilizes and
# further applications of these rules cause no seats to change state!
# Once people stop moving around, you count 37 occupied seats.
#
# Simulate your seating area by applying the seating rules repeatedly
# until no seats change state. How many seats end up occupied?
#
#
# --- Solution ---
#
# First we read the input file as a 2-dimensional array of single characters.
# Then in a loop, we copy current array (grid) and process every element in it
# to satisfy the mentioned rules. We break the loop when there was no change.
# The key here is find the neighbors of a current seat (position in grid)
# properly – taking into account that some elements does not exist on the
# edges. For this we use a function that returns some default value instead
# of IndexError or in case of negative indexes (this emulates get() method
# from the dictionaries in Python).
#

INPUT_FILE = 'input.txt'

EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'
FLOOR = '.'


def safe_grid_get(array, index_y, index_x, default=None):
    if index_y < 0 or index_x < 0:
        return default
    try:
        return array[index_y][index_x]
    except IndexError:
        return default


def can_be_occupied(grid, x, y):
    neighbors = [
        safe_grid_get(grid, y - 1, x - 1),
        safe_grid_get(grid, y - 1, x),
        safe_grid_get(grid, y - 1, x + 1),
        safe_grid_get(grid, y, x - 1),
        safe_grid_get(grid, y, x + 1),
        safe_grid_get(grid, y + 1, x - 1),
        safe_grid_get(grid, y + 1, x),
        safe_grid_get(grid, y + 1, x + 1)
    ]

    if OCCUPIED_SEAT in neighbors:
        return False
    else:
        return True


def shall_be_free(grid, x, y):
    neighbors = [
        safe_grid_get(grid, y - 1, x - 1),
        safe_grid_get(grid, y - 1, x),
        safe_grid_get(grid, y - 1, x + 1),
        safe_grid_get(grid, y, x - 1),
        safe_grid_get(grid, y, x + 1),
        safe_grid_get(grid, y + 1, x - 1),
        safe_grid_get(grid, y + 1, x),
        safe_grid_get(grid, y + 1, x + 1)
    ]

    if neighbors.count(OCCUPIED_SEAT) >= 4:
        return True
    else:
        return False


def main():
    grid = [list(line.strip('\n')) for line in open(INPUT_FILE, 'r')]

    size_x = len(grid[0])
    size_y = len(grid)

    while True:
        new_grid = [row[:] for row in grid]
        changed = False

        for y in range(size_y):
            for x in range(size_x):
                if grid[y][x] == EMPTY_SEAT and can_be_occupied(grid, x, y):
                    new_grid[y][x] = OCCUPIED_SEAT
                    changed = True
                elif grid[y][x] == OCCUPIED_SEAT and shall_be_free(grid, x, y):
                    new_grid[y][x] = EMPTY_SEAT
                    changed = True

        if changed:
            grid = new_grid
        else:
            break

    print(sum([row.count(OCCUPIED_SEAT) for row in grid]))


if __name__ == '__main__':
    main()
