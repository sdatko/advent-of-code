#!/usr/bin/env python3
#
# --- Day 21: Allergen Assessment / Part Two ---
#
# Now that you've isolated the inert ingredients, you should have enough
# information to figure out which ingredient contains which allergen.
#
# In the above example:
#
#   mxmxvkd contains dairy.
#   sqjhc contains fish.
#   fvjkl contains soy.
#
# Arrange the ingredients alphabetically by their allergen and separate
# them by commas to produce your canonical dangerous ingredient list.
# (There should not be any spaces in your canonical dangerous ingredient list.)
# In the above example, this would be mxmxvkd,sqjhc,fvjkl.
#
# Time to stock your raft with supplies.
# What is your canonical dangerous ingredient list?
#
#
# --- Solution ---
#
# The difference here is that we need to join the names of unsafe ingredients,
# sorted alphabetically by their correspoding allergen. After the detection
# procedure from part 1 done, this is basically about sorting the dictionary
# items by their values and joing the keys from produced arrangement.
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

    canonical_dangerous_ingredient_list = ','.join(
        ingredient
        for ingredient, allergen in sorted(allergens.items(),
                                           key=lambda item: item[1])
    )

    print(canonical_dangerous_ingredient_list)


if __name__ == '__main__':
    main()
