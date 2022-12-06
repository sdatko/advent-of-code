#!/usr/bin/env python3
#
# --- Day 6: Tuning Trouble / Part Two ---
#
# Your device's communication system is correctly detecting packets, but
# still isn't working. It looks like it also needs to look for messages.
#
# A start-of-message marker is just like a start-of-packet marker,
# except it consists of 14 distinct characters rather than 4.
#
# Here are the first positions of start-of-message markers for all
# of the above examples:
# – mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
# – bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
# – nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
# – nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
# – zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26
#
# How many characters need to be processed before the first start-of-message
# marker is detected?
#
#
# --- Solution ---
#
# The whole difference here is that we need to take bigger window.
# The rest of the code is exactly the same as for part 1.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        data = file.read().strip()

    window_size = 14

    for index in range(len(data) - window_size + 1):
        marker = set(data[index:index + window_size])
        if len(marker) == window_size:
            break

    print(index + window_size)


if __name__ == '__main__':
    main()
