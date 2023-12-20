#!/usr/bin/env python3
#
# --- Day 20: Pulse Propagation / Part Two ---
#
# The final machine responsible for moving the sand down to Island Island
# has a module attached named rx. The machine turns on when a single
# low pulse is sent to rx.
#
# Reset all modules to their default states. Waiting for all pulses to be
# fully handled after each button press, what is the fewest number of button
# presses required to deliver a single low pulse to the module named rx?
#
#
# --- Solution ---
#
# The difference here is that we need to a perform button pressing until there
# is a low state signal sent to the desired module rx. The catch is – it takes
# very, very long until that happens. After examining the input file we can
# notice that the final state is triggered by a single conjunction, which is
# triggered earlier by a couple of other conjunctions. Since conjunctions
# behave like the NAND gate, they require all inputs to be in high state
# before they will produce the wanted outcome, instead we can keep tracking
# how many presses it will take to put those other conjunctions in right state.
# Then, as the signals going through modules are periodic (as in part 1)
# we can find the necessary number of presses for the rx module by calculating
# the lowest common multiplication of presses needed by rx module sources.
#

INPUT_FILE = 'input.txt'

CONJUNCTION = '&'
FLIPFLOP = '%'

START_MODULE = 'broadcaster'
START_STATE = 0

END_STATE = 'rx'


def gcd(numbers: list[int]) -> int:
    numbers = list(numbers)

    while len(numbers) > 1:
        number1 = numbers.pop()
        number2 = numbers.pop()

        while number2:
            number1, number2 = number2, number1 % number2

        numbers.append(number1)  # save the divisor

    return numbers.pop()


def lcm(numbers: list[int]) -> int:
    multipled = numbers[0]

    for number in numbers[1:]:
        multipled *= number / gcd(numbers)

    return int(multipled)


def main():
    with open(INPUT_FILE, 'r') as file:
        modules = [line.split(' -> ')
                   for line in file.read().strip().split('\n')]

        flipflops = {name.strip(FLIPFLOP): 0
                     for name, _ in modules
                     if name.startswith(FLIPFLOP)}
        conjunctions = {name.strip(CONJUNCTION): {}
                        for name, _ in modules
                        if name.startswith(CONJUNCTION)}
        modules = {name.strip(FLIPFLOP).strip(CONJUNCTION): output.split(', ')
                   for name, output in modules}

        for conjunction in conjunctions:
            watched = {name: 0
                       for name in modules
                       if conjunction in modules[name]}
            conjunctions[conjunction] = watched

    source_of_end_state = [name
                           for name, output in modules.items()
                           if END_STATE in output][0]

    states_to_watch = conjunctions[source_of_end_state].copy()

    presses = 0

    while True:
        # Button pressed
        presses += 1
        states = [(START_MODULE, START_STATE, None)]

        # Signal propagates
        while states:
            name, level, source = states.pop(0)

            if name not in modules:  # there is nothing more, signal stops
                continue

            elif name in flipflops:
                if level == 1:  # nothing happens, signal stops
                    continue

                else:  # switch signal on-off
                    flipflops[name] = int(not flipflops[name])
                    level = flipflops[name]

            elif name in conjunctions:
                conjunctions[name][source] = level

                if all(conjunctions[name].values()):  # all inputs positive
                    level = 0
                else:
                    level = 1

            # generate outputs
            for output in modules[name]:
                states.append((output, level, name))

            # save if we reached the high state on one of the desired outputs
            if name in states_to_watch.keys() and level == 1:
                states_to_watch[name] = presses

        if all(states_to_watch.values()):  # we found what we need
            break

    print(lcm(tuple(states_to_watch.values())))


if __name__ == '__main__':
    main()
