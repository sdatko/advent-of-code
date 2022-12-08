#!/usr/bin/env python3
#
# --- Day 8: Treetop Tree House / Part Two ---
#
# Content with the amount of tree cover available, the Elves just need to know
# the best spot to build their tree house: they would like to be able to see
# a lot of trees.
#
# To measure the viewing distance from a given tree, look up, down, left,
# and right from that tree; stop if you reach an edge or at the first tree
# that is the same height or taller than the tree under consideration.
# (If a tree is right on the edge, at least one of its viewing distances
# will be zero.)
#
# The Elves don't care about distant trees taller than those found by the rules
# above; the proposed tree house has large eaves to keep it dry, so they
# wouldn't be able to see higher than the tree house anyway.
#
# In the example above, consider the middle 5 in the second row:
#
#   30373
#   25512
#   65332
#   33549
#   35390
#
# – Looking up, its view is not blocked; it can see 1 tree (of height 3).
# – Looking left, its view is blocked immediately; it can see only 1 tree
#   (of height 5, right next to it).
# – Looking right, its view is not blocked; it can see 2 trees.
# – Looking down, its view is blocked eventually; it can see 2 trees
#   (one of height 3, then the tree of height 5 that blocks its view).
#
# A tree's scenic score is found by multiplying together its viewing distance
# in each of the four directions. For this tree, this is 4
# (found by multiplying 1 * 1 * 2 * 2).
#
# However, you can do even better: consider the tree of height 5 in the middle
# of the fourth row:
#
#   30373
#   25512
#   65332
#   33549
#   35390
#
# – Looking up, its view is blocked at 2 trees (by another tree with
#   a height of 5).
# – Looking left, its view is not blocked; it can see 2 trees.
# – Looking down, its view is also not blocked; it can see 1 tree.
# – Looking right, its view is blocked at 2 trees (by a massive tree
#   of height 9).
#
# This tree's scenic score is 8 (2 * 2 * 1 * 2);
# this is the ideal spot for the tree house.
#
# Consider each tree on your map. What is the highest scenic score possible
# for any tree?
#
#
# --- Solution ---
#
# The difference here is that we need to find how far in each direction
# there is a tree that is bigger or equal to any currently examined (i, j).
# Provided that such one exists there, we find its index in the vector of trees
# in a given directions (counting +1, as *that* tree would be also visible
# from the house perspective), otherwise we count the whole distance to the
# edge of the forest. Then we calculate the scenic score for a given element
# (i, j) and we return the highest found as an answer.
# Note that for convenience the vectors of trees to the left and to the top
# of a given element (i, j) were reversed, so we need to find the first element
# that does not meet the condition, just like for the vectors to the right
# and to the bottom.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        trees = tuple([tuple(map(int, list(row.strip())))
                       for row in file.read().strip().split()])

    scores = []

    for i, row in enumerate(trees):
        for j, col in enumerate(row):
            element = trees[i][j]

            top = tuple(reversed([element > row[j] for row in trees[:i]]))
            left = tuple(reversed([element > col for col in trees[i][:j]]))
            right = tuple([element > col for col in trees[i][j + 1:]])
            bottom = tuple([element > row[j] for row in trees[i + 1:]])

            to_top = \
                top.index(False) + 1 if (False in top) else len(top)
            to_left = \
                left.index(False) + 1 if (False in left) else len(left)
            to_right = \
                right.index(False) + 1 if (False in right) else len(right)
            to_bottom = \
                bottom.index(False) + 1 if (False in bottom) else len(bottom)

            score = to_top * to_left * to_right * to_bottom
            scores.append(score)

    print(max(scores))


if __name__ == '__main__':
    main()
