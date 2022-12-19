#!/usr/bin/env python3
#
# --- Day 19: Not Enough Minerals / Part Two ---
#
# While you were choosing the best blueprint, the elephants found some food
# on their own, so you're not in as much of a hurry; you figure you probably
# have 32 minutes before the wind changes direction again and you'll need
# to get out of range of the erupting volcano.
#
# Unfortunately, one of the elephants ate most of your blueprint list!
# Now, only the first three blueprints in your list are intact.
#
# In 32 minutes, the largest number of geodes blueprint 1 (from the example
# above) can open is 56. One way to achieve that is:
#
#   == Minute 1 ==
#   1 ore-collecting robot collects 1 ore; you now have 1 ore.
#
#   == Minute 2 ==
#   1 ore-collecting robot collects 1 ore; you now have 2 ore.
#
#   == Minute 3 ==
#   1 ore-collecting robot collects 1 ore; you now have 3 ore.
#
#   == Minute 4 ==
#   1 ore-collecting robot collects 1 ore; you now have 4 ore.
#
#   == Minute 5 ==
#   Spend 4 ore to start building an ore-collecting robot.
#   1 ore-collecting robot collects 1 ore; you now have 1 ore.
#   The new ore-collecting robot is ready; you now have 2 of them.
#
#   == Minute 6 ==
#   2 ore-collecting robots collect 2 ore; you now have 3 ore.
#
#   == Minute 7 ==
#   Spend 2 ore to start building a clay-collecting robot.
#   2 ore-collecting robots collect 2 ore; you now have 3 ore.
#   The new clay-collecting robot is ready; you now have 1 of them.
#
#   == Minute 8 ==
#   Spend 2 ore to start building a clay-collecting robot.
#   2 ore-collecting robots collect 2 ore; you now have 3 ore.
#   1 clay-collecting robot collects 1 clay; you now have 1 clay.
#   The new clay-collecting robot is ready; you now have 2 of them.
#
#   == Minute 9 ==
#   Spend 2 ore to start building a clay-collecting robot.
#   2 ore-collecting robots collect 2 ore; you now have 3 ore.
#   2 clay-collecting robots collect 2 clay; you now have 3 clay.
#   The new clay-collecting robot is ready; you now have 3 of them.
#
#   == Minute 10 ==
#   Spend 2 ore to start building a clay-collecting robot.
#   2 ore-collecting robots collect 2 ore; you now have 3 ore.
#   3 clay-collecting robots collect 3 clay; you now have 6 clay.
#   The new clay-collecting robot is ready; you now have 4 of them.
#
#   == Minute 11 ==
#   Spend 2 ore to start building a clay-collecting robot.
#   2 ore-collecting robots collect 2 ore; you now have 3 ore.
#   4 clay-collecting robots collect 4 clay; you now have 10 clay.
#   The new clay-collecting robot is ready; you now have 5 of them.
#
#   == Minute 12 ==
#   Spend 2 ore to start building a clay-collecting robot.
#   2 ore-collecting robots collect 2 ore; you now have 3 ore.
#   5 clay-collecting robots collect 5 clay; you now have 15 clay.
#   The new clay-collecting robot is ready; you now have 6 of them.
#
#   == Minute 13 ==
#   Spend 2 ore to start building a clay-collecting robot.
#   2 ore-collecting robots collect 2 ore; you now have 3 ore.
#   6 clay-collecting robots collect 6 clay; you now have 21 clay.
#   The new clay-collecting robot is ready; you now have 7 of them.
#
#   == Minute 14 ==
#   Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
#   2 ore-collecting robots collect 2 ore; you now have 2 ore.
#   7 clay-collecting robots collect 7 clay; you now have 14 clay.
#   The new obsidian-collecting robot is ready; you now have 1 of them.
#
#   == Minute 15 ==
#   2 ore-collecting robots collect 2 ore; you now have 4 ore.
#   7 clay-collecting robots collect 7 clay; you now have 21 clay.
#   1 obsidian-collecting robot collects 1 obsidian; you now have 1 obsidian.
#
#   == Minute 16 ==
#   Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
#   2 ore-collecting robots collect 2 ore; you now have 3 ore.
#   7 clay-collecting robots collect 7 clay; you now have 14 clay.
#   1 obsidian-collecting robot collects 1 obsidian; you now have 2 obsidian.
#   The new obsidian-collecting robot is ready; you now have 2 of them.
#
#   == Minute 17 ==
#   Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
#   2 ore-collecting robots collect 2 ore; you now have 2 ore.
#   7 clay-collecting robots collect 7 clay; you now have 7 clay.
#   2 obsidian-collecting robots collect 2 obsidian; you now have 4 obsidian.
#   The new obsidian-collecting robot is ready; you now have 3 of them.
#
#   == Minute 18 ==
#   2 ore-collecting robots collect 2 ore; you now have 4 ore.
#   7 clay-collecting robots collect 7 clay; you now have 14 clay.
#   3 obsidian-collecting robots collect 3 obsidian; you now have 7 obsidian.
#
#   == Minute 19 ==
#   Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
#   2 ore-collecting robots collect 2 ore; you now have 3 ore.
#   7 clay-collecting robots collect 7 clay; you now have 7 clay.
#   3 obsidian-collecting robots collect 3 obsidian; you now have 10 obsidian.
#   The new obsidian-collecting robot is ready; you now have 4 of them.
#
#   == Minute 20 ==
#   Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
#   2 ore-collecting robots collect 2 ore; you now have 3 ore.
#   7 clay-collecting robots collect 7 clay; you now have 14 clay.
#   4 obsidian-collecting robots collect 4 obsidian; you now have 7 obsidian.
#   The new geode-cracking robot is ready; you now have 1 of them.
#
#   == Minute 21 ==
#   Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
#   2 ore-collecting robots collect 2 ore; you now have 2 ore.
#   7 clay-collecting robots collect 7 clay; you now have 7 clay.
#   4 obsidian-collecting robots collect 4 obsidian; you now have 11 obsidian.
#   1 geode-cracking robot cracks 1 geode; you now have 1 open geode.
#   The new obsidian-collecting robot is ready; you now have 5 of them.
#
#   == Minute 22 ==
#   Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
#   2 ore-collecting robots collect 2 ore; you now have 2 ore.
#   7 clay-collecting robots collect 7 clay; you now have 14 clay.
#   5 obsidian-collecting robots collect 5 obsidian; you now have 9 obsidian.
#   1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.
#   The new geode-cracking robot is ready; you now have 2 of them.
#
#   == Minute 23 ==
#   Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
#   2 ore-collecting robots collect 2 ore; you now have 2 ore.
#   7 clay-collecting robots collect 7 clay; you now have 21 clay.
#   5 obsidian-collecting robots collect 5 obsidian; you now have 7 obsidian.
#   2 geode-cracking robots crack 2 geodes; you now have 4 open geodes.
#   The new geode-cracking robot is ready; you now have 3 of them.
#
#   == Minute 24 ==
#   Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
#   2 ore-collecting robots collect 2 ore; you now have 2 ore.
#   7 clay-collecting robots collect 7 clay; you now have 28 clay.
#   5 obsidian-collecting robots collect 5 obsidian; you now have 5 obsidian.
#   3 geode-cracking robots crack 3 geodes; you now have 7 open geodes.
#   The new geode-cracking robot is ready; you now have 4 of them.
#
#   == Minute 25 ==
#   2 ore-collecting robots collect 2 ore; you now have 4 ore.
#   7 clay-collecting robots collect 7 clay; you now have 35 clay.
#   5 obsidian-collecting robots collect 5 obsidian; you now have 10 obsidian.
#   4 geode-cracking robots crack 4 geodes; you now have 11 open geodes.
#
#   == Minute 26 ==
#   Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
#   2 ore-collecting robots collect 2 ore; you now have 4 ore.
#   7 clay-collecting robots collect 7 clay; you now have 42 clay.
#   5 obsidian-collecting robots collect 5 obsidian; you now have 8 obsidian.
#   4 geode-cracking robots crack 4 geodes; you now have 15 open geodes.
#   The new geode-cracking robot is ready; you now have 5 of them.
#
#   == Minute 27 ==
#   Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
#   2 ore-collecting robots collect 2 ore; you now have 4 ore.
#   7 clay-collecting robots collect 7 clay; you now have 49 clay.
#   5 obsidian-collecting robots collect 5 obsidian; you now have 6 obsidian.
#   5 geode-cracking robots crack 5 geodes; you now have 20 open geodes.
#   The new geode-cracking robot is ready; you now have 6 of them.
#
#   == Minute 28 ==
#   2 ore-collecting robots collect 2 ore; you now have 6 ore.
#   7 clay-collecting robots collect 7 clay; you now have 56 clay.
#   5 obsidian-collecting robots collect 5 obsidian; you now have 11 obsidian.
#   6 geode-cracking robots crack 6 geodes; you now have 26 open geodes.
#
#   == Minute 29 ==
#   Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
#   2 ore-collecting robots collect 2 ore; you now have 6 ore.
#   7 clay-collecting robots collect 7 clay; you now have 63 clay.
#   5 obsidian-collecting robots collect 5 obsidian; you now have 9 obsidian.
#   6 geode-cracking robots crack 6 geodes; you now have 32 open geodes.
#   The new geode-cracking robot is ready; you now have 7 of them.
#
#   == Minute 30 ==
#   Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
#   2 ore-collecting robots collect 2 ore; you now have 6 ore.
#   7 clay-collecting robots collect 7 clay; you now have 70 clay.
#   5 obsidian-collecting robots collect 5 obsidian; you now have 7 obsidian.
#   7 geode-cracking robots crack 7 geodes; you now have 39 open geodes.
#   The new geode-cracking robot is ready; you now have 8 of them.
#
#   == Minute 31 ==
#   Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
#   2 ore-collecting robots collect 2 ore; you now have 6 ore.
#   7 clay-collecting robots collect 7 clay; you now have 77 clay.
#   5 obsidian-collecting robots collect 5 obsidian; you now have 5 obsidian.
#   8 geode-cracking robots crack 8 geodes; you now have 47 open geodes.
#   The new geode-cracking robot is ready; you now have 9 of them.
#
#   == Minute 32 ==
#   2 ore-collecting robots collect 2 ore; you now have 8 ore.
#   7 clay-collecting robots collect 7 clay; you now have 84 clay.
#   5 obsidian-collecting robots collect 5 obsidian; you now have 10 obsidian.
#   9 geode-cracking robots crack 9 geodes; you now have 56 open geodes.
#
# However, blueprint 2 from the example above is still better; using it,
# the largest number of geodes you could open in 32 minutes is 62.
#
# You no longer have enough blueprints to worry about quality levels.
# Instead, for each of the first three blueprints, determine the largest
# number of geodes you could open; then, multiply these three values together.
#
# Don't worry about quality levels; instead, just determine the largest
# number of geodes you could open using each of the first three blueprints.
# What do you get if you multiply these numbers together?
#
#
# --- Solution ---
#
# The difference here is that we consider a smaller number of blueprints,
# but for each one we need to take a longer time into account. The final
# answer is calculated according to a little different formula (involving
# multiplication, not sum).
# Exact code from part 1 worked here well enough, however I was unsatisfied
# with the performance and not-proven properties, so I experimented with other
# approaches. The one given finally here is a DFS algorithm, which turned out
# to be a little more efficient. It uses the same optimisations as described
# in part 1 code, in addition to the skipping of already explored states.
#

INPUT_FILE = 'input.txt'

NUMBER_OF_BLUEPRINTS = 3
TOTAL_TIME = 32

INITIAL_ORE = 0
INITIAL_CLAY = 0
INITIAL_OBSIDIAN = 0
INITIAL_GEODE = 0

ROBOTS_ORE = 1
ROBOTS_CLAY = 0
ROBOTS_OBSIDIAN = 0
ROBOTS_GEODE = 0

INDEX = {
    'ore': 1,
    'clay': 2,
    'obsidian': 3,
    'geode': 4,
}


def main():
    with open(INPUT_FILE, 'r') as file:
        blueprints = [blueprint.split(';')
                      for blueprint in file.read()
                                           .replace('Blueprint ', '')
                                           .replace('Each ', '')
                                           .replace(' robot costs ', ';')
                                           .replace(' and ', ' ')
                                           .replace(': ', ';')
                                           .replace('. ', ';')
                                           .replace('.', '')
                                           .strip()
                                           .split('\n')]
        blueprints = {int(blueprint[0]): blueprint[1:]
                      for blueprint in blueprints[:NUMBER_OF_BLUEPRINTS]}
        blueprints = {ID: {recipe[2 * i]: recipe[2 * i + 1].split(' ')
                           for i in range(len(recipe) // 2)}
                      for ID, recipe in blueprints.items()}
        blueprints = {ID: {item: {ingredients[2 * i + 1]:
                                  int(ingredients[2 * i])
                                  for i in range(len(ingredients) // 2)}
                           for item, ingredients in recipe.items()}
                      for ID, recipe in blueprints.items()}

    total_geodes_multiplied = 1

    for blueprintID, blueprint in blueprints.items():
        maxes = {}
        for item in blueprint.keys():
            maxes[item] = max(requirement.get(item, 0)
                              for requirement in blueprint.values())
        max_geodes = 0
        CACHE = set()

        states = set([(
            TOTAL_TIME,
            INITIAL_ORE, INITIAL_CLAY, INITIAL_OBSIDIAN, INITIAL_GEODE,
            ROBOTS_ORE, ROBOTS_CLAY, ROBOTS_OBSIDIAN, ROBOTS_GEODE,
        )])

        while states:
            state = states.pop()

            # if already seen that, skip it
            if state in CACHE:
                continue
            CACHE.add(state)

            # we reached the time limit, save the current best result
            if state[0] <= 0:
                max_geodes = max(state[4], max_geodes)
                continue

            # drop state if it cannot be better than the current best one
            time_left = state[0]
            Sn = (2 * state[8] + time_left - 1) * time_left / 2
            if (state[4] + Sn) < max_geodes:
                continue

            # collect resources (helper step for calculations)
            tmp_state = list(state)
            tmp_state[0] -= 1
            tmp_state[1] += tmp_state[5]
            tmp_state[2] += tmp_state[6]
            tmp_state[3] += tmp_state[7]
            tmp_state[4] += tmp_state[8]

            # build nothing
            new_state = tmp_state.copy()
            states.add(tuple(new_state))

            # attempt building a geode robot
            requirements = blueprint['geode']
            if all(state[INDEX[requirement]] >= amount
                   for requirement, amount in requirements.items()):
                new_state = tmp_state.copy()
                new_state[8] += 1
                for requirement, amount in requirements.items():
                    new_state[INDEX[requirement]] -= amount
                states.add(tuple(new_state))

            # attempt building a obsidian robot
            requirements = blueprint['obsidian']
            if all(state[INDEX[requirement]] >= amount
                   for requirement, amount in requirements.items()) \
               and state[7] < maxes['obsidian']:
                new_state = tmp_state.copy()
                new_state[7] += 1
                for requirement, amount in requirements.items():
                    new_state[INDEX[requirement]] -= amount
                states.add(tuple(new_state))

            # attempt building a clay robot
            requirements = blueprint['clay']
            if all(state[INDEX[requirement]] >= amount
                   for requirement, amount in requirements.items()) \
               and state[6] < maxes['clay']:
                new_state = tmp_state.copy()
                new_state[6] += 1
                for requirement, amount in requirements.items():
                    new_state[INDEX[requirement]] -= amount
                states.add(tuple(new_state))

            # attempt building a ore robot
            requirements = blueprint['ore']
            if all(state[INDEX[requirement]] >= amount
                   for requirement, amount in requirements.items()) \
               and state[5] < maxes['ore']:
                new_state = tmp_state.copy()
                new_state[5] += 1
                for requirement, amount in requirements.items():
                    new_state[INDEX[requirement]] -= amount
                states.add(tuple(new_state))

        # simulation has ended – save current max number of geodes
        total_geodes_multiplied *= max_geodes

    print(total_geodes_multiplied)


if __name__ == '__main__':
    main()
