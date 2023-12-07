#!/usr/bin/env python3
#
# --- Day 4: Security Through Obscurity / Part Two ---
#
# With all the decoy data out of the way,
# it's time to decrypt this list and get moving.
#
# The room names are encrypted by a state-of-the-art shift cipher,
# which is nearly unbreakable without the right software. However,
# the information kiosk designers at Easter Bunny HQ were not expecting
# to deal with a master cryptographer like yourself.
#
# To decrypt a room name, rotate each letter forward through the alphabet
# a number of times equal to the room's sector ID. A becomes B, B becomes C,
# Z becomes A, and so on. Dashes become spaces.
#
# For example, the real name for `qzmt-zixmtkozy-ivhz-343`
# is `very encrypted name`.
#
# What is the sector ID of the room where North Pole objects are stored?
#
#
# --- Solution ---
#
# The difference here is that for all real rooms (with correct rooms)
# we need to decrypt the room name and find the ID of a room that name
# matches the searched text (the `north pole`, without space). For this
# the helper function was prepared, that finds numeric value for each
# character, shifts it by the given key value and converts back to character.
#

INPUT_FILE = 'input.txt'

SEARCHED_TEXT = 'northpole'


def decrypt(word: str, key: int) -> str:
    return ''.join([chr((ord(character) - ord('a') + key) % 26 + ord('a'))
                    for character in word])


def main():
    with open(INPUT_FILE, 'r') as file:
        rooms = [line.split('-')
                 for line in file.read()
                                 .strip()
                                 .replace('[', '-')
                                 .replace(']', '')
                                 .split('\n')]

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
            real_name = ' '.join([decrypt(word, ID)
                                  for word in room[:-2]])

            if real_name.find(SEARCHED_TEXT) >= 0:
                break

    print(ID)


if __name__ == '__main__':
    main()
