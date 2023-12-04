#!/usr/bin/env python3
#
# --- Day 4: Repose Record / Part Two ---
#
# Strategy 2: Of all guards, which guard is most frequently asleep
# on the same minute?
#
# In the example above, Guard #99 spent minute 45 asleep more than
# any other guard or minute - three times in total. (In all other cases,
# any guard spent any minute asleep at most twice.)
#
# What is the ID of the guard you chose multiplied by the minute you chose?
# (In the above example, the answer would be 99 * 45 = 4455.)
#
#
# --- Solution ---
#
# With current implementation, the only difference here is the condition
# for finding the answer – we want to identify the guard, that falls asleep
# most frequently at the same minute (max). Finally the answer is calculated
# and returned the same way as in previous part.
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
        top = max(guards[guard_id])

        if top > most:
            most = top
            answer = guard_id * guards[guard_id].index(top)

    print(answer)


if __name__ == '__main__':
    main()
