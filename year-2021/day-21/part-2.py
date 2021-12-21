#!/usr/bin/env python3
#
# Task:
# Now that you're warmed up, it's time to play the real game.
# A second compartment opens, this time labeled Dirac dice. Out of it falls
# a single three-sided die.
# As you experiment with the die, you feel a little strange. An informational
# brochure in the compartment explains that this is a quantum die: when you
# roll it, the universe splits into multiple copies, one copy for each possible
# outcome of the die. In this case, rolling the die always splits the universe
# into three copies: one where the outcome of the roll was 1, one where it was
# 2, and one where it was 3.
# The game is played the same as before, although to prevent things from
# getting too far out of hand, the game now ends when either player's score
# reaches at least 21.
# Using the same starting positions as in the example above,
# player 1 wins in 444356092776315 universes, while player 2 merely wins
# in 341960390180808 universes.
# Using your given starting positions, determine every possible outcome.
# Find the player that wins in more universes; in how many universes
# does that player win?
#
# Solution:
# This is mostly a start from scratch... First we count the possible outcomes
# from a 3 rolls and how many these outcomes happen. Then we prepare a function
# that will simulate every possible way the game will go. At given positions,
# scores and turn, for each possible rolls outcome, we calculate new results
# and two things may happen: either we finish the game with the new scores,
# or we should simulate recurrently the game with a new set of conditions.
# As a result, we simply count the numbers of times there was a win for each
# of all possible rolls. After about 30 seconds it gives us the right answer.
#

INPUT_FILE = 'input.txt'

GOAL = 21

PLAYER_1 = 0
PLAYER_2 = 1

CACHE = {}


def game(possibilities, positions, scores, turn=0):
    uuid = ((tuple(positions), tuple(scores), turn))
    if uuid in CACHE:
        return CACHE[uuid]

    player = PLAYER_1 if turn % 2 == 0 else PLAYER_2
    turn += 1
    wins = [0, 0]

    for roll, times in possibilities.items():
        new_positions = positions.copy()
        new_scores = scores.copy()

        new_position = (positions[player] + roll) % 10

        new_positions[player] = new_position
        new_scores[player] += (new_position + 1)

        if new_scores[PLAYER_1] < GOAL and new_scores[PLAYER_2] < GOAL:
            win1, win2 = game(possibilities, new_positions, new_scores, turn)
            wins[0] += win1 * times
            wins[1] += win2 * times
        else:
            if new_scores[PLAYER_1] >= GOAL:
                wins[PLAYER_1] += times
            else:
                wins[PLAYER_2] += times

    CACHE[uuid] = wins
    return wins


def main():
    positions = [int(line.strip().split()[-1]) - 1
                 for line in open(INPUT_FILE, 'r')]
    scores = [0, 0]

    possibilities = {}  # 3x roll result -> how many times it can happen
    for dice1 in [1, 2, 3]:
        for dice2 in [1, 2, 3]:
            for dice3 in [1, 2, 3]:
                result = dice1 + dice2 + dice3
                if result not in possibilities:
                    possibilities[result] = 1
                else:
                    possibilities[result] += 1

    wins = game(possibilities, positions, scores, turn=0)

    print(max(wins))


if __name__ == '__main__':
    main()
