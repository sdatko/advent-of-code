#!/usr/bin/env python3
#
# --- Day 7: Camel Cards / Part Two ---
#
# To make things a little more interesting, the Elf introduces one additional
# rule. Now, J cards are jokers - wildcards that can act like whatever card
# would make the hand the strongest type possible.
#
# To balance this, J cards are now the weakest individual cards, weaker even
# than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5,
# 4, 3, 2, J.
#
# J cards can pretend to be whatever card is best for the purpose of
# determining hand type; for example, QJJQ2 is now considered four of a kind.
# However, for the purpose of breaking ties between two hands of the same type,
# J is always treated as J, not the card it's pretending to be: JKKK2 is weaker
# than QQQQ2 because J is weaker than Q.
#
# Now, the above example goes very differently:
#
#   32T3K 765
#   T55J5 684
#   KK677 28
#   KTJJT 220
#   QQQJA 483
#
# – 32T3K is still the only one pair; it doesn't contain any jokers,
#   so its strength doesn't increase.
# – KK677 is now the only two pair, making it the second-weakest hand.
# – T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3,
#   QQQJA gets rank 4, and KTJJT gets rank 5.
#
# With the new joker rule, the total winnings in this example are 5905.
#
# Using the new joker rule, find the rank of every hand in your set.
# What are the new total winnings?
#
#
# --- Solution ---
#
# The only difference here is that we move the 'J' to the end of order list.
# Then, when determining the kind of cards, we count the number of jokers
# in hand and add that number to the counts, then we discard all jokers cards
# from the counts. The condition for full house requires additional check
# for case of two pairs and one joker. Also there was a special case where
# all cards were jokers. The rest of the code remains absolutely the same.
#

INPUT_FILE = 'input.txt'

ORDER = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
ORDER.reverse()


def kind(cards):
    jokers = cards.count('J')
    counts = {card: cards.count(card) + jokers
              for card in set(cards)}

    if 'J' in counts:
        del counts['J']

    # Five of a kind
    if len(counts) == 1 or jokers == 5:
        return 6

    # Four of a kind
    if max(counts.values()) == 4:
        return 5

    # Full house
    if sorted(counts.values()) == [2, 3] or sorted(counts.values()) == [3, 3]:
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
