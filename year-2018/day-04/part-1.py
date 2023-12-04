#!/usr/bin/env python3
#
# --- Day 4: Repose Record ---
#
# You've sneaked into another supply closet - this time, it's across from
# the prototype suit manufacturing lab. You need to sneak inside and fix
# the issues with the suit, but there's a guard stationed outside the lab,
# so this is as close as you can safely get.
#
# As you search the closet for anything that might help, you discover that
# you're not the first person to want to sneak in. Covering the walls,
# someone has spent an hour starting every midnight for the past few months
# secretly observing this guard post! They've been writing down the ID
# of the one guard on duty that night - the Elves seem to have decided
# that one guard was enough for the overnight shift - as well as when they
# fall asleep or wake up while at their post (your puzzle input).
#
# For example, consider the following records, which have already
# been organized into chronological order:
#
#   [1518-11-01 00:00] Guard #10 begins shift
#   [1518-11-01 00:05] falls asleep
#   [1518-11-01 00:25] wakes up
#   [1518-11-01 00:30] falls asleep
#   [1518-11-01 00:55] wakes up
#   [1518-11-01 23:58] Guard #99 begins shift
#   [1518-11-02 00:40] falls asleep
#   [1518-11-02 00:50] wakes up
#   [1518-11-03 00:05] Guard #10 begins shift
#   [1518-11-03 00:24] falls asleep
#   [1518-11-03 00:29] wakes up
#   [1518-11-04 00:02] Guard #99 begins shift
#   [1518-11-04 00:36] falls asleep
#   [1518-11-04 00:46] wakes up
#   [1518-11-05 00:03] Guard #99 begins shift
#   [1518-11-05 00:45] falls asleep
#   [1518-11-05 00:55] wakes up
#
# Timestamps are written using year-month-day hour:minute format.
# The guard falling asleep or waking up is always the one whose shift
# most recently started. Because all asleep/awake times are during
# the midnight hour (00:00 - 00:59), only the minute portion (00 - 59)
# is relevant for those events.
#
# Visually, these records show that the guards are asleep at these times:
#
#   Date   ID   Minute
#               000000000011111111112222222222333333333344444444445555555555
#               012345678901234567890123456789012345678901234567890123456789
#   11-01  #10  .....####################.....#########################.....
#   11-02  #99  ........................................##########..........
#   11-03  #10  ........................#####...............................
#   11-04  #99  ....................................##########..............
#   11-05  #99  .............................................##########.....
#
# The columns are Date, which shows the month-day portion of the relevant day;
# ID, which shows the guard on duty that day; and Minute, which shows
# the minutes during which the guard was asleep within the midnight hour.
# (The Minute column's header shows the minute's ten's digit in the first row
# and the one's digit in the second row.) Awake is shown as ., and asleep
# is shown as #.
#
# Note that guards count as asleep on the minute they fall asleep, and they
# count as awake on the minute they wake up. For example, because Guard #10
# wakes up at 00:25 on 1518-11-01, minute 25 is marked as awake.
#
# If you can figure out the guard most likely to be asleep at a specific time,
# you might be able to trick that guard into working tonight so you can have
# the best chance of sneaking in. You have two strategies for choosing
# the best guard/minute combination.
#
# Strategy 1: Find the guard that has the most minutes asleep.
# What minute does that guard spend asleep the most?
#
# In the example above, Guard #10 spent the most minutes asleep, a total of
# 50 minutes (20+25+5), while Guard #99 only slept for a total of 30 minutes
# (10+10+10). Guard #10 was asleep most during minute 24 (on two days,
# whereas any other minute the guard was asleep was only seen on one day).
#
# While this example listed the entries in chronological order, your entries
# are in the order you found them. You'll need to organize them before they
# can be analyzed.
#
# What is the ID of the guard you chose multiplied by the minute you chose?
# (In the above example, the answer would be 10 * 24 = 240.)
#
#
# --- Solution ---
#
# We start by reading the input file into a list of logs/strings, removing all
# unnecessary elements first, such as brackets, colons and a redundant text,
# e.g. `[1518-11-03 00:24] falls asleep` would become `1518-11-03 00 24 falls`.
# Then we process the logs in a loop – for each log, we determine the action
# depending on the last field, which can be `fall`, `wakes` or a number.
# In case of the last, we set the guard ID and create a dictionary entry
# where we counts the minutes while the guard sleeps (if necessary).
# In case of `falls`, we save the start time from third column; and in case
# of `wakes` we save end time from the same column, additionally taking notes
# on what minutes the current guard was sleeping. After that, we need to find
# the guard that slept the most according to all processed logs and identify
# the minute most common for that guard to sleep. Finally, as an answer
# we return the guard ID with the identified minute.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        logs = sorted(file.read().strip()
                                 .replace('[', '')
                                 .replace(':', ' ')
                                 .replace(']', '')
                                 .replace('Guard #', '')
                                 .replace(' begins shift', '')
                                 .replace(' asleep', '')
                                 .replace(' up', '')
                                 .split('\n'))

    guards = {}
    ID = None

    for log in logs:
        day, hour, minute, action = log.split()

        if action == 'falls':
            t_start = int(minute)

        elif action == 'wakes':
            t_end = int(minute)

            for time in range(t_start, t_end):
                guards[ID][time] += 1

        else:  # guard begins shift
            ID = int(action)

            if ID not in guards:
                guards[ID] = [0] * 60

    most = 0

    for guard_id in guards:
        total = sum(guards[guard_id])

        if total > most:
            most = total
            top = max(guards[guard_id])
            answer = guard_id * guards[guard_id].index(top)

    print(answer)


if __name__ == '__main__':
    main()
