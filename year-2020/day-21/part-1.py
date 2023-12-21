#!/usr/bin/env python3
#
# --- Day 21: Allergen Assessment ---
#
# You reach the train's last stop and the closest you can get to your vacation
# island without getting wet. There aren't even any boats here, but nothing
# can stop you now: you build a raft. You just need a few days' worth of food
# for your journey.
#
# You don't speak the local language, so you can't read any ingredients lists.
# However, sometimes, allergens are listed in a language you do understand.
# You should be able to use this information to determine which ingredient
# contains which allergen and work out which foods are safe to take with you
# on your trip.
#
# You start by compiling a list of foods (your puzzle input), one food per
# line. Each line includes that food's ingredients list followed by some
# or all of the allergens the food contains.
#
# Each allergen is found in exactly one ingredient. Each ingredient contains
# zero or one allergen. Allergens aren't always marked; when they're listed
# (as in (contains nuts, shellfish) after an ingredients list), the ingredient
# that contains each listed allergen will be somewhere in the corresponding
# ingredients list. However, even if an allergen isn't listed, the ingredient
# that contains that allergen could still be present: maybe they forgot to
# label it, or maybe it was labeled in a language you don't know.
#
# For example, consider the following list of foods:
#
#   mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
#   trh fvjkl sbzzf mxmxvkd (contains dairy)
#   sqjhc fvjkl (contains soy)
#   sqjhc mxmxvkd sbzzf (contains fish)
#
# The first food in the list has four ingredients (written in a language
# you don't understand): mxmxvkd, kfcds, sqjhc, and nhms. While the food
# might contain other allergens, a few allergens the food definitely
# contains are listed afterward: dairy and fish.
#
# The first step is to determine which ingredients can't possibly contain
# any of the allergens in any food in your list. In the above example,
# none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen.
# Counting the number of times any of these ingredients appear in any
# ingredients list produces 5: they all appear once each except sbzzf,
# which appears twice.
#
# Determine which ingredients cannot possibly contain any of the allergens
# in your list. How many times do any of those ingredients appear?
#
#
# --- Solution ---
#
# We start by reading the input file into a list of foods, each consisting of
# a set of ingredients and a set of allergens, by splitting over newlines and
# then each line on phrase ` (contains `. Then we produce a dictionary of all
# allergens and their possible ingredients by selecting all ingredients sets
# that had each allergen listed and calculating their intersection to narrow
# the candidates. Assuming this task is solvable, after that there must be
# at least one allergen that has only one ingredient candidate listed. Hence,
# in a loop, as long as there are some allergens left to be decoded, we find
# such one with exactly one candidate and we store it in a separate collection
# of allergens matched with ingredients. Additionally we remove such allergen
# from the ones to be decoded and from all remaining allergens to be decoded
# we remove the associated ingredient. Then there will appear new allergen
# that will have exactly one candidate from now on... After repeating such
# steps several times, we decoded all the allergens to their corresponding
# ingredients name, so we can generate a set of forbidden ingredients.
# What remains is to go through list of foods and find a set of only safe
# ingredients for each food ingredients using set operations (subtraction).
# Finally, as an answer, we return the total number of safe ingredients found.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        foods = [line.rstrip(')').split(' (contains ')
                 for line in file.read().strip().split('\n')]
        foods = tuple((set(ingredients.split()), set(allergens.split(', ')))
                      for ingredients, allergens in foods)

    allergens_to_decode = {allergen: {}
                           for _, allergens in foods
                           for allergen in allergens}

    for allergen in allergens_to_decode:
        ingredients_containing_allergen = [ingredients
                                           for ingredients, allergens in foods
                                           if allergen in allergens]

        candidates = set.intersection(*ingredients_containing_allergen)
        allergens_to_decode[allergen] = candidates

    allergens = {}

    while allergens_to_decode:
        for allergen, ingredients in allergens_to_decode.copy().items():
            if len(ingredients) == 1:
                ingredient = next(iter(ingredients))
                allergens[ingredient] = allergen

                del allergens_to_decode[allergen]

                for key in allergens_to_decode:
                    allergens_to_decode[key].discard(ingredient)

    forbidden_ingredients = set(allergens.keys())

    number_of_safe_ingredients = 0

    for ingredients, _ in foods:
        safe_ingredients = ingredients - forbidden_ingredients
        number_of_safe_ingredients += len(safe_ingredients)

    print(number_of_safe_ingredients)


if __name__ == '__main__':
    main()
