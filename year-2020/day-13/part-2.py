#!/usr/bin/env python3
#
# Task:
# The shuttle company is running a contest: one gold coin for anyone that can
# find the earliest timestamp such that the first bus ID departs at that time
# and each subsequent listed bus ID departs at that subsequent minute.
# (The first line in your input is no longer relevant.)
# An x in the schedule means there are no constraints on what bus IDs must
# depart at that time. (we can ignore that entry in calculations)
# For example input 7,13,x,x,59,x,31,19 you are looking for the earliest
# timestamp (called t) such that:
# - Bus ID 7 departs at timestamp t.
# - Bus ID 13 departs one minute after timestamp t.
# - There are no requirements or restrictions on departures at two or three
#   minutes after timestamp t.
# - Bus ID 59 departs four minutes after timestamp t.
# - There are no requirements or restrictions on departures at five minutes
#   after timestamp t.
# - Bus ID 31 departs six minutes after timestamp t.
# - Bus ID 19 departs seven minutes after timestamp t.
# What is the earliest timestamp such that all of the listed bus IDs depart
# at offsets matching their positions in the list?
#
# Solution:
# From the input file we read the data and interpret them as bus schedules
# and offsets between the considered buses. Such data can then be represented
# as a set of equation as follows:
# ( time + offset[i] )  %  schedule[i]  =  0
# which is exact to:
# time  %  schedule[i]  =  ( schedule[i] - offset[i] )  % schedule[i]
# which can be simplified to the following:
# time  %  schedule[i]  =  rests[i]
# The task is to find the lowest value of time that satisfies all of the given
# equations in a set. Here we can simply apply the Chinese remainder theorem
# to find such value in efficient time.
# Python 3.8+ required for pow() with negative exponent while provided modulo.
#

INPUT_FILE = 'input.txt'


def main():
    schedule = []
    offsets = []
    rests = []

    with open(INPUT_FILE, 'r') as input_file:
        input_file.readline()  # skip first line

        offset = 0
        for time in input_file.readline().strip().split(','):
            if time != 'x':
                schedule.append(int(time))
                offsets.append(offset)
                rests.append(-offset % int(time))
            offset += 1

    upper_bound = 1
    for element in schedule:
        upper_bound *= element

    sum_of_multiplied_residues = 0
    for divisor, rest in zip(schedule, rests):
        multiplied_divisors = upper_bound // divisor
        sum_of_multiplied_residues += (
            rest * multiplied_divisors * pow(multiplied_divisors, -1, divisor)
        )

    print(sum_of_multiplied_residues % upper_bound)


if __name__ == '__main__':
    main()
