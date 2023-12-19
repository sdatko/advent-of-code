#!/usr/bin/env python3
#
# --- Day 19: Aplenty / Part Two ---
#
# Even with your help, the sorting process still isn't fast enough.
#
# One of the Elves comes up with a new plan: rather than sort parts
# individually through all of these workflows, maybe you can figure out
# in advance which combinations of ratings will be accepted or rejected.
#
# Each of the four ratings (x, m, a, s) can have an integer value
# ranging from a minimum of 1 to a maximum of 4000. Of all possible
# distinct combinations of ratings, your job is to figure out which ones
# will be accepted.
#
# In the above example, there are 167409079868000 distinct combinations
# of ratings that will be accepted.
#
# Consider only your list of workflows; the list of part ratings that
# the Elves wanted you to sort is no longer relevant. How many distinct
# combinations of ratings will be accepted by the Elves' workflows?
#
#
# --- Solution ---
#
# The difference here is that here we need to find a solution not for given
# input ranges from file, but for all possible combinations of values of x,
# m, a and s – which is 256_000_000_000_000 possibilities. This numbers is
# to large for iterative verification of each combination, hence what we need
# to do is to work on ranges of values for all parameters. Starting on initial
# ('in', {'x': (1, 4000), 'y': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}),
# for a given example workflow `in{s<1351:px,qqz}` we would produce two groups:
# ('px', {'x': (1, 4000), 'y': (1, 4000), 'a': (1, 4000), 's': (1, 1350)}),
# ('qqz', {'x': (1, 4000), 'y': (1, 4000), 'a': (1, 4000), 's': (1351, 4000)}).
# We continue such processing and divisions until we obtain there a group with
# either accepted or rejected workflow name. Finally, we can return the number
# of combinations by summarizing counts of values within all accepted ranges.
#
# The change of ranges can be neatly presented with so called Sankey diagrams.
#

INPUT_FILE = 'input.txt'

ACCEPTED = 'A'
REJECTED = 'R'
STARTING_WORKFLOW_NAME = 'in'
STARTING_RANGE = (1, 4000)


def evaluate2(rules: tuple[str], ranges: dict) -> list[tuple[str, dict]]:
    results = []

    # modify ranges for all but last rule
    for rule in rules[:-1]:
        condition, workflow_name = rule.split(':')
        variable = condition[0]
        operator = condition[1]
        treshold = int(condition[2:])

        variable_min, variable_max = ranges[variable]

        # divide ranges and keep what remains
        if variable_min < treshold < variable_max:
            new_ranges = ranges.copy()

            if operator == '<':
                new_ranges[variable] = (variable_min, treshold - 1)
                ranges[variable] = (treshold, variable_max)

                result = (workflow_name, new_ranges)
                results.append(result)

            else:  # operator == '>'
                new_ranges[variable] = (treshold + 1, variable_max)
                ranges[variable] = (variable_min, treshold)

                result = (workflow_name, new_ranges)
                results.append(result)

        elif treshold <= variable_min and operator == '>':
            result = (workflow_name, ranges)
            results.append(result)

            return results  # nothing remains

        elif variable_max <= treshold and operator == '<':
            result = (workflow_name, ranges)
            results.append(result)

            return results  # nothing remains

    # for what remains, return with the workflow name from last rule
    workflow_name = rules[-1]
    result = (workflow_name, ranges)
    results.append(result)

    return results


def main():
    with open(INPUT_FILE, 'r') as file:
        workflows, _ = file.read().strip().split('\n\n')

        workflows = [tuple(workflow.split('{'))
                     for workflow in workflows.replace('}', '').split('\n')]
        workflows = {name: rules.split(',')
                     for name, rules in workflows}

    parts_to_process = [
        (STARTING_WORKFLOW_NAME, {variable: STARTING_RANGE
                                  for variable in ('x', 'm', 'a', 's')})
    ]

    accepted_parts = []
    combinations = 0

    while parts_to_process:
        workflow_name, ranges = parts_to_process.pop()

        results = evaluate2(workflows[workflow_name], ranges)

        for result in results:
            workflow_name, _ = result

            if workflow_name not in (ACCEPTED, REJECTED):
                parts_to_process.append(result)

            elif workflow_name == ACCEPTED:
                accepted_parts.append(result)

    for accepted_part in accepted_parts:
        _, ranges = accepted_part
        combinations_in_range = 1

        for range_start, range_end in ranges.values():
            combinations_in_range *= (range_end - range_start + 1)

        combinations += combinations_in_range

    print(combinations)


if __name__ == '__main__':
    main()
