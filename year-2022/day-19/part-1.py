#!/usr/bin/env python3
#
# --- Day 19: Not Enough Minerals ---
#
# Your scans show that the lava did indeed form obsidian!
#
# The wind has changed direction enough to stop sending lava droplets
# toward you, so you and the elephants exit the cave. As you do, you notice
# a collection of geodes around the pond. Perhaps you could use the obsidian
# to create some geode-cracking robots and break them open?
#
# To collect the obsidian from the bottom of the pond, you'll need waterproof
# obsidian-collecting robots. Fortunately, there is an abundant amount of clay
# nearby that you can use to make them waterproof.
#
# In order to harvest the clay, you'll need special-purpose clay-collecting
# robots. To make any type of robot, you'll need ore, which is also plentiful
# but in the opposite direction from the clay.
#
# Collecting ore requires ore-collecting robots with big drills. Fortunately,
# you have exactly one ore-collecting robot in your pack that you can use
# to kickstart the whole operation.
#
# Each robot can collect 1 of its resource type per minute. It also takes
# one minute for the robot factory (also conveniently from your pack)
# to construct any type of robot, although it consumes the necessary
# resources available when construction begins.
#
# The robot factory has many blueprints (your puzzle input) you can choose
# from, but once you've configured it with a blueprint, you can't change it.
# You'll need to work out which blueprint is best.
#
# For example:
#
#   Blueprint 1:
#     Each ore robot costs 4 ore.
#     Each clay robot costs 2 ore.
#     Each obsidian robot costs 3 ore and 14 clay.
#     Each geode robot costs 2 ore and 7 obsidian.
#
#   Blueprint 2:
#     Each ore robot costs 2 ore.
#     Each clay robot costs 3 ore.
#     Each obsidian robot costs 3 ore and 8 clay.
#     Each geode robot costs 3 ore and 12 obsidian.
#
# (Blueprints have been line-wrapped here for legibility. The robot factory's
# actual assortment of blueprints are provided one blueprint per line.)
#
# The elephants are starting to look hungry, so you shouldn't take too long;
# you need to figure out which blueprint would maximize the number of opened
# geodes after 24 minutes by figuring out which robots to build and when
# to build them.
#
# Using blueprint 1 in the example above, the largest number of geodes you
# could open in 24 minutes is 9. One way to achieve that is:
#
#   == Minute 1 ==
#   1 ore-collecting robot collects 1 ore; you now have 1 ore.
#
#   == Minute 2 ==
#   1 ore-collecting robot collects 1 ore; you now have 2 ore.
#
#   == Minute 3 ==
#   Spend 2 ore to start building a clay-collecting robot.
#   1 ore-collecting robot collects 1 ore; you now have 1 ore.
#   The new clay-collecting robot is ready; you now have 1 of them.
#
#   == Minute 4 ==
#   1 ore-collecting robot collects 1 ore; you now have 2 ore.
#   1 clay-collecting robot collects 1 clay; you now have 1 clay.
#
#   == Minute 5 ==
#   Spend 2 ore to start building a clay-collecting robot.
#   1 ore-collecting robot collects 1 ore; you now have 1 ore.
#   1 clay-collecting robot collects 1 clay; you now have 2 clay.
#   The new clay-collecting robot is ready; you now have 2 of them.
#
#   == Minute 6 ==
#   1 ore-collecting robot collects 1 ore; you now have 2 ore.
#   2 clay-collecting robots collect 2 clay; you now have 4 clay.
#
#   == Minute 7 ==
#   Spend 2 ore to start building a clay-collecting robot.
#   1 ore-collecting robot collects 1 ore; you now have 1 ore.
#   2 clay-collecting robots collect 2 clay; you now have 6 clay.
#   The new clay-collecting robot is ready; you now have 3 of them.
#
#   == Minute 8 ==
#   1 ore-collecting robot collects 1 ore; you now have 2 ore.
#   3 clay-collecting robots collect 3 clay; you now have 9 clay.
#
#   == Minute 9 ==
#   1 ore-collecting robot collects 1 ore; you now have 3 ore.
#   3 clay-collecting robots collect 3 clay; you now have 12 clay.
#
#   == Minute 10 ==
#   1 ore-collecting robot collects 1 ore; you now have 4 ore.
#   3 clay-collecting robots collect 3 clay; you now have 15 clay.
#
#   == Minute 11 ==
#   Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
#   1 ore-collecting robot collects 1 ore; you now have 2 ore.
#   3 clay-collecting robots collect 3 clay; you now have 4 clay.
#   The new obsidian-collecting robot is ready; you now have 1 of them.
#
#   == Minute 12 ==
#   Spend 2 ore to start building a clay-collecting robot.
#   1 ore-collecting robot collects 1 ore; you now have 1 ore.
#   3 clay-collecting robots collect 3 clay; you now have 7 clay.
#   1 obsidian-collecting robot collects 1 obsidian; you now have 1 obsidian.
#   The new clay-collecting robot is ready; you now have 4 of them.
#
#   == Minute 13 ==
#   1 ore-collecting robot collects 1 ore; you now have 2 ore.
#   4 clay-collecting robots collect 4 clay; you now have 11 clay.
#   1 obsidian-collecting robot collects 1 obsidian; you now have 2 obsidian.
#
#   == Minute 14 ==
#   1 ore-collecting robot collects 1 ore; you now have 3 ore.
#   4 clay-collecting robots collect 4 clay; you now have 15 clay.
#   1 obsidian-collecting robot collects 1 obsidian; you now have 3 obsidian.
#
#   == Minute 15 ==
#   Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
#   1 ore-collecting robot collects 1 ore; you now have 1 ore.
#   4 clay-collecting robots collect 4 clay; you now have 5 clay.
#   1 obsidian-collecting robot collects 1 obsidian; you now have 4 obsidian.
#   The new obsidian-collecting robot is ready; you now have 2 of them.
#
#   == Minute 16 ==
#   1 ore-collecting robot collects 1 ore; you now have 2 ore.
#   4 clay-collecting robots collect 4 clay; you now have 9 clay.
#   2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.
#
#   == Minute 17 ==
#   1 ore-collecting robot collects 1 ore; you now have 3 ore.
#   4 clay-collecting robots collect 4 clay; you now have 13 clay.
#   2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.
#
#   == Minute 18 ==
#   Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
#   1 ore-collecting robot collects 1 ore; you now have 2 ore.
#   4 clay-collecting robots collect 4 clay; you now have 17 clay.
#   2 obsidian-collecting robots collect 2 obsidian; you now have 3 obsidian.
#   The new geode-cracking robot is ready; you now have 1 of them.
#
#   == Minute 19 ==
#   1 ore-collecting robot collects 1 ore; you now have 3 ore.
#   4 clay-collecting robots collect 4 clay; you now have 21 clay.
#   2 obsidian-collecting robots collect 2 obsidian; you now have 5 obsidian.
#   1 geode-cracking robot cracks 1 geode; you now have 1 open geode.
#
#   == Minute 20 ==
#   1 ore-collecting robot collects 1 ore; you now have 4 ore.
#   4 clay-collecting robots collect 4 clay; you now have 25 clay.
#   2 obsidian-collecting robots collect 2 obsidian; you now have 7 obsidian.
#   1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.
#
#   == Minute 21 ==
#   Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
#   1 ore-collecting robot collects 1 ore; you now have 3 ore.
#   4 clay-collecting robots collect 4 clay; you now have 29 clay.
#   2 obsidian-collecting robots collect 2 obsidian; you now have 2 obsidian.
#   1 geode-cracking robot cracks 1 geode; you now have 3 open geodes.
#   The new geode-cracking robot is ready; you now have 2 of them.
#
#   == Minute 22 ==
#   1 ore-collecting robot collects 1 ore; you now have 4 ore.
#   4 clay-collecting robots collect 4 clay; you now have 33 clay.
#   2 obsidian-collecting robots collect 2 obsidian; you now have 4 obsidian.
#   2 geode-cracking robots crack 2 geodes; you now have 5 open geodes.
#
#   == Minute 23 ==
#   1 ore-collecting robot collects 1 ore; you now have 5 ore.
#   4 clay-collecting robots collect 4 clay; you now have 37 clay.
#   2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.
#   2 geode-cracking robots crack 2 geodes; you now have 7 open geodes.
#
#   == Minute 24 ==
#   1 ore-collecting robot collects 1 ore; you now have 6 ore.
#   4 clay-collecting robots collect 4 clay; you now have 41 clay.
#   2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.
#   2 geode-cracking robots crack 2 geodes; you now have 9 open geodes.
#
# However, by using blueprint 2 in the example above, you could do even better:
# the largest number of geodes you could open in 24 minutes is 12.
#
# Determine the quality level of each blueprint by multiplying that blueprint's
# ID number with the largest number of geodes that can be opened in 24 minutes
# using that blueprint. In this example, the first blueprint has ID 1 and can
# open 9 geodes, so its quality level is 9. The second blueprint has ID 2 and
# can open 12 geodes, so its quality level is 24. Finally, if you add up
# the quality levels of all of the blueprints in the list, you get 33.
#
# Determine the quality level of each blueprint using the largest number
# of geodes it could produce in 24 minutes. What do you get if you add up
# the quality level of all of the blueprints in your list?
#
#
# --- Solution ---
#
# We start by reading the input into a dictionary of blueprints, each one
# identified by ID and containing a specification (inner dictionary)
# of resources necessary to build robots. This part is complex, as I did not
# assume every droid would require similar resources (i.e. every geode robot
# requires ores and obsidians, just the needed amount is different).
# Then comes the loop over the blueprints, for each blueprint figuring out
# the maximum number of geodes obtainable within a given time limit.
# The approach here is a BFS algorithm: for each time step, we discover every
# possible outcome from the set of currently available states, considering
# that we may build nothing and just wait, as well as that we build any robot
# we can afford with current resources. There are two most important additions
# to make this approach finishing in finite time:
# – for a given blueprint, we calculate the highest number of each unit we may
#   ever need: as during single round we can only build up to one robot,
#   producing more resources each round than needed would be a waste,
# – for a given state, we estimate how many geodes we potentially can reach,
#   assuming optimistically each round of time left we will get more geodes,
#   i.e. for 5 time units left and 3 geode robots currently in possession,
#   we may get 3, 4, 5, 6 and 7 geodes per round, so up to 25 geodes in total;
#   if this number if lower than the currently known maximum, there is no way
#   from a given state we can beat the maximum and we shall skip it anyway.
#   In short, the formula for the sum of an arithmetic sequence can be applied.
# Finally, after reaching the end of search, we multiply the maximum reached
# number of geodes by the blueprint ID and add that as quality level.
# The sum after processing all blueprints is our answer.
# This approach needs about 2-3 seconds for blueprint, providing an answer
# withing about 1-2 minutes. Replacing `if (state[3] + Sn) < max_geodes`
# with `if state[3] < max_geodes` accelerates the search a little, but it does
# not work universally (e.g. the answer for blueprint 10 is wrong; however
# `max_geodes - 1` is enough for my input and resolved part 2 in a matter
# of seconds – but I am cannot justify that with 100% confidence).
#

INPUT_FILE = 'input.txt'

NUMBER_OF_BLUEPRINTS = 30
TOTAL_TIME = 24

INITIAL_ORE = 0
INITIAL_CLAY = 0
INITIAL_OBSIDIAN = 0
INITIAL_GEODE = 0

ROBOTS_ORE = 1
ROBOTS_CLAY = 0
ROBOTS_OBSIDIAN = 0
ROBOTS_GEODE = 0

INDEX = {
    'ore': 0,
    'clay': 1,
    'obsidian': 2,
    'geode': 3,
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

    total_quality_level = 0

    for blueprintID, blueprint in blueprints.items():
        maxes = {}
        for item in blueprint.keys():
            maxes[item] = max(requirement.get(item, 0)
                              for requirement in blueprint.values())
        max_geodes = 0

        states = set([(
            INITIAL_ORE, INITIAL_CLAY, INITIAL_OBSIDIAN, INITIAL_GEODE,
            ROBOTS_ORE, ROBOTS_CLAY, ROBOTS_OBSIDIAN, ROBOTS_GEODE,
        )])

        for i in range(TOTAL_TIME):
            new_states = set()
            time_left = TOTAL_TIME - i

            for state in states:
                # drop states that cannot be better than the current best one
                Sn = (2 * state[7] + time_left - 1) * time_left / 2
                if (state[3] + Sn) < max_geodes:
                    continue

                # collect resources (helper step for calculations)
                tmp_state = list(state)
                tmp_state[0] += tmp_state[4]
                tmp_state[1] += tmp_state[5]
                tmp_state[2] += tmp_state[6]
                tmp_state[3] += tmp_state[7]

                # build nothing
                new_state = tmp_state.copy()
                new_states.add(tuple(new_state))

                # attempt building a geode robot
                requirements = blueprint['geode']
                if all(state[INDEX[requirement]] >= amount
                       for requirement, amount in requirements.items()):
                    new_state = tmp_state.copy()
                    new_state[7] += 1
                    for requirement, amount in requirements.items():
                        new_state[INDEX[requirement]] -= amount
                    new_states.add(tuple(new_state))

                # attempt building a obsidian robot
                requirements = blueprint['obsidian']
                if all(state[INDEX[requirement]] >= amount
                       for requirement, amount in requirements.items()) \
                   and state[6] < maxes['obsidian']:
                    new_state = tmp_state.copy()
                    new_state[6] += 1
                    for requirement, amount in requirements.items():
                        new_state[INDEX[requirement]] -= amount
                    new_states.add(tuple(new_state))

                # attempt building a clay robot
                requirements = blueprint['clay']
                if all(state[INDEX[requirement]] >= amount
                       for requirement, amount in requirements.items()) \
                   and state[5] < maxes['clay']:
                    new_state = tmp_state.copy()
                    new_state[5] += 1
                    for requirement, amount in requirements.items():
                        new_state[INDEX[requirement]] -= amount
                    new_states.add(tuple(new_state))

                # attempt building a ore robot
                requirements = blueprint['ore']
                if all(state[INDEX[requirement]] >= amount
                       for requirement, amount in requirements.items()) \
                   and state[4] < maxes['ore']:
                    new_state = tmp_state.copy()
                    new_state[4] += 1
                    for requirement, amount in requirements.items():
                        new_state[INDEX[requirement]] -= amount
                    new_states.add(tuple(new_state))

            states = new_states
            max_geodes = max(state[3] for state in states)

        # simulation has ended – save current max number of geodes
        total_quality_level += max_geodes * blueprintID

    print(total_quality_level)


if __name__ == '__main__':
    main()
