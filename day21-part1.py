#!/home/tromer/advent-of-code-2020/venv/bin/python3

import re
import sys

from collections import defaultdict


def main():
  allergen_ingredient_sets = defaultdict(list)
  all_allergens = set()
  all_ingredients = set()
  for line in sys.stdin:
    line = line.strip()
    ingr_str, allergen_str = re.search(r'^(.*) \(contains (.*)\)$', line).groups()
    ingredients = ingr_str.split(' ')
    all_ingredients |= set(ingredients)
    allergens = allergen_str.split(', ')
    all_allergens |= set(allergens)
    for allergen in allergens:
      allergen_ingredient_sets[allergen].append(set(ingredients))
  print(f'all ingr {all_ingredients}')
  print(f'all allergens {all_allergens}')
  for allergen in allergen_ingredient_sets.keys():
    all_ingredients = set(allergen_ingredient_sets[allergen][0])
    candidate_ingredients = set(allergen_ingredient_sets[allergen][0])
    for ingredient_set in allergen_ingredient_sets[allergen][1:]:
      candidate_ingredients &= ingredient_set
      all_ingredients |= ingredient_set
    non_allergenic_ingredients = all_ingredients - candidate_ingredients
    print(f'no {allergen} in {non_allergenic_ingredients}')

  for allergen in allergen_ingredient_sets.keys():
    candidate_ingredients = all_ingredients.copy()
    print(f'{allergen} is in one of {candidate_ingredients}')
    for ingredient_set in allergen_ingredient_sets[allergen]:
      print(f'intersect with {ingredient_set}')
      candidate_ingredients &= ingredient_set
      print(f'{allergen} is in one of {candidate_ingredients}')
    print(f'{allergen} is in one of {candidate_ingredients}')
    
    

if __name__ == "__main__":
    main()