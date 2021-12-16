#!/usr/bin/env python3
#
# Task:
# Now that you have the structure of your transmission decoded, you can
# calculate the value of the expression it represents.
# Literal values (type ID 4) represent a single number as described above.
# The remaining type IDs are more interesting:
# - Packets with type ID 0 are sum packets - their value is the sum of
#   the values of their sub-packets. If they only have a single sub-packet,
#   their value is the value of the sub-packet.
# - Packets with type ID 1 are product packets - their value is the result
#   of multiplying together the values of their sub-packets. If they only
#   have a single sub-packet, their value is the value of the sub-packet.
# - Packets with type ID 2 are minimum packets - their value is the minimum
#   of the values of their sub-packets.
# - Packets with type ID 3 are maximum packets - their value is the maximum
#   of the values of their sub-packets.
# - Packets with type ID 5 are greater than packets - their value is 1
#   if the value of the first sub-packet is greater than the value of
#   the second sub-packet; otherwise, their value is 0. These packets
#   always have exactly two sub-packets.
# - Packets with type ID 6 are less than packets - their value is 1
#   if the value of the first sub-packet is less than the value of
#   the second sub-packet; otherwise, their value is 0. These packets
#   always have exactly two sub-packets.
# - Packets with type ID 7 are equal to packets - their value is 1
#   if the value of the first sub-packet is equal to the value of
#   the second sub-packet; otherwise, their value is 0. These packets
#   always have exactly two sub-packets.
# Using these rules, you can now work out the value of the outermost packet
# in your BITS transmission.
# For example:
# - C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
# - 04005AC33890 finds the product of 6 and 9, resulting in the value 54.
# - 880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
# - CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
# - D8005AC2A8F0 produces 1, because 5 is less than 15.
# - F600BC2D8F produces 0, because 5 is not greater than 15.
# - 9C005AC2F8F0 produces 0, because 5 is not equal to 15.
# - 9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.
# What do you get if you evaluate the expression represented by your
# hexadecimal-encoded BITS transmission?
#
# Solution:
# Having the previous part done properly, this part is a piece of cake.
# We just need to introduce additional conditions in case of type ID equal
# to 4 – for operator packets. Then perform one of 7 actions on the values
# returned by nested calls to process subpackets. We may also drop saving
# the packet version as it is not needed in the part anymore.
# Having done that, the outcome of outermost call to processing function
# will return the desired answer.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        transmission = file.read().strip()
    bits = ''.join([format(int(char, 16), '04b') for char in transmission])

    def process(bits):
        _, bits = int(bits[:3], 2), bits[3:]
        typeID, bits = int(bits[:3], 2), bits[3:]

        if typeID == 4:  # literal value
            part, bits = bits[:5], bits[5:]
            value_str = part[1:]

            while part[0] != '0':
                part, bits = bits[:5], bits[5:]
                value_str += part[1:]

            value = int(value_str, 2)

            return value, bits

        else:  # operator
            lengthtypeID, bits = int(bits[:1], 2), bits[1:]
            values = []

            if lengthtypeID == 0:
                length = 15
            else:
                length = 11

            number, bits = int(bits[:length], 2), bits[length:]

            if lengthtypeID == 0:
                subpackets, bits = bits[:number], bits[number:]

                while len(subpackets) >= 11:
                    value, subpackets = process(subpackets)
                    values.append(value)

            else:
                for i in range(number):
                    value, bits = process(bits)
                    values.append(value)

            if typeID == 0:
                value = sum(values)
            elif typeID == 1:
                value = 1
                for val in values:
                    value *= val
            elif typeID == 2:
                value = min(values)
            elif typeID == 3:
                value = max(values)
            elif typeID == 5:
                value = int(values[0] > values[1])
            elif typeID == 6:
                value = int(values[0] < values[1])
            elif typeID == 7:
                value = int(values[0] == values[1])

            return value, bits

    value, bits = process(bits)

    print(value)


if __name__ == '__main__':
    main()
