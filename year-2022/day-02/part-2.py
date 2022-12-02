#!/usr/bin/env python3
#
# --- Day 2: Rock Paper Scissors / Part Two ---
#
# The Elf finishes helping with the tent and sneaks back over to you.
# "Anyway, the second column says how the round needs to end: X means
# you need to lose, Y means you need to end the round in a draw,
# and Z means you need to win. Good luck!"
#
# The total score is still calculated in the same way, but now you need
# to figure out what shape to choose so the round ends as indicated.
# The example above now goes like this:
# – In the first round, your opponent will choose Rock (A), and you need
#   the round to end in a draw (Y), so you also choose Rock. This gives you
#   a score of 1 + 3 = 4.
# – In the second round, your opponent will choose Paper (B), and you choose
#   Rock so you lose (X) with a score of 1 + 0 = 1.
# – In the third round, you will defeat your opponent's Scissors with Rock
#   for a score of 1 + 6 = 7.
#
# Now that you're correctly decrypting the ultra top secret strategy guide,
# you would get a total score of 12.
#
# Following the Elf's instructions for the second column, what would your
# total score be if everything goes exactly according to your strategy guide?
#
#
# --- Solution ---
#
# The difference here is how we interpret the second value (our choice).
# In this case, this is symbol that specifies the goal for us and based
# on that we need to select our choice to take – to use it finally
# in calculations of points.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        guide = [row.strip().split(' ')
                 for row in file.read().strip().split('\n')]

    points_for_shape = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    points_for_outcome = {
        'lost': 0,
        'draw': 3,
        'won': 6,
    }

    shape_to_outcome = {
        'X': 'lost',
        'Y': 'draw',
        'Z': 'won',
    }

    score = 0

    for opponents, ours in guide:
        goal = shape_to_outcome[ours]

        if goal == 'draw':
            if opponents == 'A':
                pick = 'X'
            if opponents == 'B':
                pick = 'Y'
            if opponents == 'C':
                pick = 'Z'

        if goal == 'won':
            if opponents == 'A':
                pick = 'Y'
            if opponents == 'B':
                pick = 'Z'
            if opponents == 'C':
                pick = 'X'

        if goal == 'lost':
            if opponents == 'A':
                pick = 'Z'
            if opponents == 'B':
                pick = 'X'
            if opponents == 'C':
                pick = 'Y'

        score += points_for_shape[pick]
        score += points_for_outcome[goal]

    print(score)


if __name__ == '__main__':
    main()
