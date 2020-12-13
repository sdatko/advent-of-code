#!/usr/bin/env python3
#
# Task:
# To save time once you arrive, your goal is to figure out the earliest
# bus you can take to the airport. (There will be exactly one such bus.)
# What is the ID of the earliest bus you can take to the airport
# multiplied by the number of minutes you'll need to wait for that bus?
#
# Solution:
# We read the first line from the input file as a current time and then
# the next line as an array of bus lines numbers, ignoring the values 'x'.
# Then for each bus line number, we find the smallest number greater than
# current time, that is divisible by this bus line number – that would be
# the next time of departure. Then we simply multiply the difference between
# current time and the departure time by the bus line number it would be.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as input_file:
        current_time = int(input_file.readline().strip())
        schedule = [int(time)
                    for time in input_file.readline().strip().split(',')
                    if time != 'x']

    next_departures = []

    for bus_line in schedule:
        for time_to_wait in range(bus_line + 1):
            if (current_time + time_to_wait) % bus_line == 0:
                next_departures.append(time_to_wait)

    time_to_wait = min(next_departures)
    next_bus_index = next_departures.index(time_to_wait)
    next_bus_number = schedule[next_bus_index]

    print(next_bus_number * time_to_wait)


if __name__ == '__main__':
    main()
