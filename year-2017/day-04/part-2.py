#!/usr/bin/env python3
#
# --- Day 4: High-Entropy Passphrases / Part Two ---
#
# For added security, yet another system policy has been put in place.
# Now, a valid passphrase must contain no two words that are anagrams
# of each other - that is, a passphrase is invalid if any word's letters
# can be rearranged to form any other word in the passphrase.
#
# For example:
# – abcde fghij is a valid passphrase.
# – abcde xyz ecdab is not valid - the letters from the third word can be
#   rearranged to form the first word.
# – a ab abc abd abf abj is a valid passphrase, because all letters need
#   to be used when forming another word.
# – iiii oiii ooii oooi oooo is valid.
# – oiii ioii iioi iiio is not valid - any of these words can be rearranged
#   to form any other word.
#
# Under this new system policy, how many passphrases are valid?
#
#
# --- Solution ---
#
# The difference here is that instead of counting the unique words, we shall
# consider now the characters present in each word for their uniqueness.
# For each passphrase we build a list of sorted words, so we will ignore
# the original positions and take into account just the occurrences of letters,
# then we need to compare all elements with each other. If any of the elements
# are the same, i.e. at least one of the word is not unique, the passphrase
# is invalid. Finally, we return the number of valid passphrases.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        passphrases = [line.split()
                       for line in file.read().strip().split('\n')]

    valid = 0

    for passphrase in passphrases:
        words = [sorted(word) for word in passphrase]
        unique = True

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[i] == words[j]:
                    unique = False
                    break

            if not unique:
                break

        if unique:
            valid += 1

    print(valid)


if __name__ == '__main__':
    main()
