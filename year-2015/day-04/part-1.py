#!/usr/bin/env python3
#
# --- Day 4: The Ideal Stocking Stuffer ---
#
# Santa needs help mining some AdventCoins (very similar to bitcoins)
# to use as gifts for all the economically forward-thinking little
# girls and boys.

# To do this, he needs to find MD5 hashes which, in hexadecimal, start
# with at least five zeroes. The input to the MD5 hash is some secret key
# (your puzzle input, given below) followed by a number in decimal.
# To mine AdventCoins, you must find Santa the lowest positive number
# (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
#
# For example:
# – If your secret key is abcdef, the answer is 609043, because the MD5 hash
#   of abcdef609043 starts with five zeroes (000001dbbfa...), and it is
#   the lowest such number to do so.
# – If your secret key is pqrstuv, the lowest number it combines with to make
#   an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash
#   of pqrstuv1048970 looks like 000006136ef....
#
#
# --- Solution ---
#
# We start by reading the secret key from the input file. Then in an infinite
# loop we attempt to find the number that appended s string to the secret key
# would produce a MD5 hash that starts with string 00000. Once such hash was
# encountered, we return the number for which it occurred.
#

INPUT_FILE = 'input.txt'


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
        key = file.read().strip()

    iteration = 0

    while True:
        md5sum = MD5(key + str(iteration))

        if md5sum.startswith('00000'):
            break

        iteration += 1

    print(iteration)


if __name__ == '__main__':
    main()
