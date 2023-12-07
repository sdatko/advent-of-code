#!/usr/bin/env python3
#
# --- Day 7: Camel Cards ---
#
# Your all-expenses-paid trip turns out to be a one-way, five-minute ride
# in an airship. (At least it's a cool airship!) It drops you off at the edge
# of a vast desert and descends back to Island Island.
#
# "Did you bring the parts?"
#
# You turn around to see an Elf completely covered in white clothing,
# wearing goggles, and riding a large camel.
#
# "Did you bring the parts?" she asks again, louder this time.
# You aren't sure what parts she's looking for; you're here to figure out
# why the sand stopped.
#
# "The parts! For the sand, yes! Come with me; I will show you."
# She beckons you onto the camel.
#
# After riding a bit across the sands of Desert Island, you can see
# what look like very large rocks covering half of the horizon.
# The Elf explains that the rocks are all along the part of Desert Island
# that is directly above Island Island, making it hard to even get there.
# Normally, they use big machines to move the rocks and filter the sand,
# but the machines have broken down because Desert Island recently stopped
# receiving the parts they need to fix the machines.
#
# You've already assumed it'll be your job to figure out why the parts
# stopped when she asks if you can help. You agree automatically.
#
# Because the journey will take a few days, she offers to teach you the game
# of Camel Cards. Camel Cards is sort of similar to poker except it's designed
# to be easier to play while riding a camel.
#
# In Camel Cards, you get a list of hands, and your goal is to order them
# based on the strength of each hand. A hand consists of five cards labeled
# one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength
# of each card follows this order, where A is the highest and 2 is the lowest.
#
# Every hand is exactly one type. From strongest to weakest, they are:
# – Five of a kind, where all five cards have the same label: AAAAA
# – Four of a kind, where four cards have the same label and one card
#   has a different label: AA8AA
# – Full house, where three cards have the same label, and the remaining
#   two cards share a different label: 23332
# – Three of a kind, where three cards have the same label, and the remaining
#   two cards are each different from any other card in the hand: TTT98
# – Two pair, where two cards share one label, two other cards share a second
#   label, and the remaining card has a third label: 23432
# – One pair, where two cards share one label, and the other three cards have
#   a different label from the pair and each other: A23A4
# – High card, where all cards' labels are distinct: 23456
#
# Hands are primarily ordered based on type; for example,
# every full house is stronger than any three of a kind.
#
# If two hands have the same type, a second ordering rule takes effect.
# Start by comparing the first card in each hand. If these cards are
# different, the hand with the stronger first card is considered stronger.
# If the first card in each hand have the same label, however, then move on
# to considering the second card in each hand. If they differ, the hand with
# the higher second card wins; otherwise, continue with the third card
# in each hand, then the fourth, then the fifth.
#
# So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger
# because its first card is stronger. Similarly, 77888 and 77788 are both
# a full house, but 77888 is stronger because its third card is stronger
# (and both hands have the same first and second card).
#
# To play Camel Cards, you are given a list of hands and their corresponding
# bid (your puzzle input). For example:
#
#   32T3K 765
#   T55J5 684
#   KK677 28
#   KTJJT 220
#   QQQJA 483
#
# This example shows five hands; each hand is followed by its bid amount.
# Each hand wins an amount equal to its bid multiplied by its rank,
# where the weakest hand gets rank 1, the second-weakest hand gets
# rank 2, and so on up to the strongest hand. Because there are five
# hands in this example, the strongest hand will have rank 5 and its
# bid will be multiplied by 5.
#
# So, the first step is to put the hands in order of strength:
# – 32T3K is the only one pair and the other hands are all a stronger type,
#   so it gets rank 1.
# – KK677 and KTJJT are both two pair. Their first cards both have the same
#   label, but the second card of KK677 is stronger (K vs T), so KTJJT gets
#   rank 2 and KK677 gets rank 3.
# – T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card,
#   so it gets rank 5 and T55J5 gets rank 4.
#
# Now, you can determine the total winnings of this set of hands by
# adding up the result of multiplying each hand's bid with its rank
# (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total
# winnings in this example are 6440.
#
# Find the rank of every hand in your set. What are the total winnings?
#
#
# --- Solution ---
#
# We start by reading the input file into a list of tuples (cards and bids).
# Then we sort that list using a custom sorting function and finally we return
# sum of ranks (positions in sorted list) multiplied by bids. The prepared
# custom sorting function, compare_hands(), first determines the kinds of both
# cards from given hands and compares them – the hands with bigger cards kind
# is considered as greater; if cards are of the same kind, then we iterate
# and compare both cards, starting from the left side, until we find the one
# that is greater according to given order. For identifying the cards kind,
# a helper function was made. It counts the occurrences of each card symbols,
# then depending on that it identifies one of the listed cases:
# – all cards were the same,
# – there were 4 the same cards,
# – exactly 2 and 3 cards were the same,
# – there were 3 the same cards,
# – exactly 2 and 3 cards were the same,
# – there were 2 the same cards,
# – all cards were different.
# Because of specification, the cmp_to_key() function was needed, so I just
# copied it from standard library in order to satisfy the no-import challenge.
#

INPUT_FILE = 'input.txt'

ORDER = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
ORDER.reverse()


def kind(cards):
    counts = {card: cards.count(card)
              for card in set(cards)}

    # Five of a kind
    if len(counts) == 1:
        return 6

    # Four of a kind
    if max(counts.values()) == 4:
        return 5

    # Full house
    if sorted(counts.values()) == [2, 3]:
        return 4

    # Three of a kind
    if max(counts.values()) == 3:
        return 3

    # Two pair
    if sorted(counts.values()) == [1, 2, 2]:
        return 2

    # One pair
    if any([value == 2 for value in counts.values()]):
        return 1

    # High card
    return 0


def compare_hands(left, right) -> int:
    cards1, _ = left
    cards2, _ = right

    kind1 = kind(cards1)
    kind2 = kind(cards2)

    if kind1 > kind2:  # left is bigger
        return 1

    elif kind1 < kind2:  # right is bigger
        return -1

    else:  # same kind -> compare card by card
        for card1, card2 in zip(cards1, cards2):
            index1 = ORDER.index(card1)
            index2 = ORDER.index(card2)

            if index1 > index2:  # left is bigger
                return 1

            elif index1 < index2:  # right is bigger
                return -1

            else:  # both cards are the same
                continue

        # all individual cards are the same
        return 0


#
# Taken from: https://github.com/python/cpython/blob/3.11/Lib/functools.py#L206
#
# Alternative: from functools import cmp_to_key
#
# No import challenge is no import challenge... ¯\_(ツ)_/¯
#
def cmp_to_key(mycmp):
    """Convert a cmp= function into a key= function"""
    class K(object):
        __slots__ = ['obj']

        def __init__(self, obj):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        __hash__ = None

    return K


def main():
    with open(INPUT_FILE, 'r') as file:
        hands = [(line.split()[0], int(line.split()[1]))
                 for line in file.read().strip().split('\n')]

    hands = sorted(hands, key=cmp_to_key(compare_hands))

    winnings = []

    for rank, (_, bid) in enumerate(hands, start=1):
        winnings.append(rank * bid)

    print(sum(winnings))


if __name__ == '__main__':
    main()
