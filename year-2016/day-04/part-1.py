#!/usr/bin/env python3
#
# --- Day 4: Security Through Obscurity ---
#
# Finally, you come across an information kiosk with a list of rooms.
# Of course, the list is encrypted and full of decoy data, but
# the instructions to decode the list are barely hidden nearby.
# Better remove the decoy data first.
#
# Each room consists of an encrypted name (lowercase letters
# separated by dashes) followed by a dash, a sector ID,
# and a checksum in square brackets.
#
# A room is real (not a decoy) if the checksum is the five most common letters
# in the encrypted name, in order, with ties broken by alphabetization.
# For example:
# – aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common
#   letters are a (5), b (3), and then a tie between x, y, and z, which
#   are listed alphabetically.
# – a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters
#   are all tied (1 of each), the first five are listed alphabetically.
# – not-a-real-room-404[oarel] is a real room.
# – totally-real-room-200[decoy] is not.
#
# Of the real rooms from the list above, the sum of their sector IDs is 1514.
#
# What is the sum of the sector IDs of the real rooms?
#
#
# --- Solution ---
#
# We start by reading the input file into a list of lists (rooms specifiers)
# by replacing bracket with dash, splitting over newlines and then splitting
# once more over dashes. Then we iterate through the rooms: the last part
# contains the checksum, the second to last contains ID and the remaining
# part of specifier is an encrypted name. First we count the occurrences
# of characters in the name, then we sort these counts and select top 5.
# If the selected 5 characters match the expected checksum, we save the ID
# as the room is real. Finally we return the sum of saved IDs.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        rooms = [line.split('-')
                 for line in file.read()
                                 .strip()
                                 .replace('[', '-')
                                 .replace(']', '')
                                 .split('\n')]

    IDs = []

    for room in rooms:
        encrypted_name = ''.join(room[:-2])
        ID = int(room[-2])
        checksum = room[-1]

        counts = {character: encrypted_name.count(character)
                  for character in encrypted_name}

        most_common = ''.join(dict(sorted(counts.items(),
                                          key=lambda item: (-item[1], item[0]),
                                          reverse=False)[:5]).keys())

        if checksum == most_common:
            IDs.append(ID)

    print(sum(IDs))


if __name__ == '__main__':
    main()
