#!/usr/bin/env python3
#
# --- Day 5: How About a Nice Game of Chess? / Part Two ---
#
# As the door slides open, you are presented with a second door that uses
# a slightly more inspired security mechanism. Clearly unimpressed by
# the last version (in what movie is the password decrypted in order?!),
# the Easter Bunny engineers have worked out a better solution.
#
# Instead of simply filling in the password from left to right, the hash
# now also indicates the position within the password to fill. You still
# look for hashes that begin with five zeroes; however, now, the sixth
# character represents the position (0-7), and the seventh character
# is the character to put in that position.
#
# A hash result of 000001f means that f is the second character
# in the password. Use only the first result for each position,
# and ignore invalid positions.
#
# For example, if the Door ID is abc:
# – The first interesting hash is from abc3231929, which produces 0000015...;
#   so, 5 goes in position 1: _5______.
# – In the previous method, 5017308 produced an interesting hash; however,
#   it is ignored, because it specifies an invalid position (8).
# – The second interesting hash is at index 5357525, which produces 000004e...;
#   so, e goes in position 4: _5__e___.
#
# You almost choke on your popcorn as the final character falls into place,
# producing the password 05ace8e3.
#
# Given the actual Door ID and this new method, what is the password? Be extra
# proud of your solution if it uses a cinematic "decrypting" animation.
#
#
# --- Solution ---
#
# The difference here is that instead of appending newly discovered characters,
# we need to set them at specific positions in the produced password. Hence,
# the initial password value with characters that would not be returned by MD5
# function call, so we can verify for sure whether the position was assigned.
# The cinematic "decrypting" animation was also prepared – every few iterations
# we display the part of just calculated hash (it changes every time in loop)
# on password positions that were not yet assigned – this gives an effect of
# randomly changing characters until a given position was there set assigned.
# The cursor hiding and showing was added for better display in terminal.
# The mechanism is enabled only on demand, so its output (that involves a lot
# of carriage returns) does not mess with the automated testing via script.
#

INPUT_FILE = 'input.txt'

ANIMATION = False


# Source of MD5 function: https://github.com/sdatko/MD5Py
def MD5(message: str) -> str:
    data = message.encode()

    def rotate_left_uint32(n: int, d: int) -> int:
        return (n << d) | (n >> (32 - d))

    S = ([7, 12, 17, 22] * 4
         + [5, 9, 14, 20] * 4
         + [4, 11, 16, 23] * 4
         + [6, 10, 15, 21] * 4)

    K = [3614090360, 3905402710, 606105819, 3250441966,
         4118548399, 1200080426, 2821735955, 4249261313,
         1770035416, 2336552879, 4294925233, 2304563134,
         1804603682, 4254626195, 2792965006, 1236535329,
         4129170786, 3225465664, 643717713, 3921069994,
         3593408605, 38016083, 3634488961, 3889429448,
         568446438, 3275163606, 4107603335, 1163531501,
         2850285829, 4243563512, 1735328473, 2368359562,
         4294588738, 2272392833, 1839030562, 4259657740,
         2763975236, 1272893353, 4139469664, 3200236656,
         681279174, 3936430074, 3572445317, 76029189,
         3654602809, 3873151461, 530742520, 3299628645,
         4096336452, 1126891415, 2878612391, 4237533241,
         1700485571, 2399980690, 4293915773, 2240044497,
         1873313359, 4264355552, 2734768916, 1309151649,
         4149444226, 3174756917, 718787259, 3951481745]

    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    data += b'\x80'
    while (len(data) % 64) != 56:
        data += b'\x00'

    data += ((len(message) * 8) % (2 ** 64)).to_bytes(length=8,
                                                      byteorder='little')

    chunks = [data[i:i + 64] for i in range(0, len(data), 64)]
    for chunk in chunks:
        M = [int.from_bytes(chunk[i:i + 4], byteorder='little')
             for i in range(0, len(chunk), 4)]

        A = a0
        B = b0
        C = c0
        D = d0

        for i in range(64):
            if 0 <= i <= 15:
                F = (B & C) | (~B & D)
                g = i
            elif 16 <= i <= 31:
                F = (B & D) | (~D & C)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                F = B ^ C ^ D
                g = (3 * i + 5) % 16
            elif 48 <= i <= 63:
                F = C ^ (B | ~D)
                g = (7 * i) % 16

            F = (F + A + K[i] + M[g]) & 0xFFFFFFFF
            A = D
            D = C
            C = B
            B = (B + rotate_left_uint32(F, S[i])) & 0xFFFFFFFF

        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF

    a0 = a0.to_bytes(length=4, byteorder='little')
    b0 = b0.to_bytes(length=4, byteorder='little')
    c0 = c0.to_bytes(length=4, byteorder='little')
    d0 = d0.to_bytes(length=4, byteorder='little')

    digest = a0 + b0 + c0 + d0

    return digest.hex()


def main():
    with open(INPUT_FILE, 'r') as file:
        ID = file.read().strip()

    password = ['_'] * 8
    iteration = 0

    if ANIMATION:
        print('\033[?25l', end='\r')  # hide cursor
        print(''.join(password), end='\r')

    while password.count('_'):
        md5sum = MD5(ID + str(iteration))

        if md5sum.startswith('00000'):
            if md5sum[5] in ['0', '1', '2', '3', '4', '5', '6', '7']:
                index = int(md5sum[5])

                if password[index] == '_':
                    password[index] = md5sum[6]

        if ANIMATION and (iteration % 50000) == 0:  # do not print too often
            for index, character in enumerate(password):
                if character == '_':
                    print(md5sum[index], end='')
                else:
                    print(character, end='')
            print('\r', end='')

        iteration += 1

    if ANIMATION:
        print('\033[?25h', end='')  # show cursor

    print(''.join(password))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ANIMATION:
            print('\033[?25h', end='')  # show cursor
