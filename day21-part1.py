#!/home/tromer/advent-of-code-2020/venv/bin/python3

import re
import sys

from collections import defaultdict


def main():
  allergen_ingredient_sets = defaultdict(list)
  all_allergens = set()
  all_ingredients = set()
  foods = []
  for line in sys.stdin:
    line = line.strip()
    ingr_str, allergen_str = re.search(r'^(.*) \(contains (.*)\)$', line).groups()
    ingredients = ingr_str.split(' ')
    all_ingredients |= set(ingredients)
    allergens = allergen_str.split(', ')
    all_allergens |= set(allergens)
    foods.append((ingredients, allergens))
    for allergen in allergens:
      allergen_ingredient_sets[allergen].append(set(ingredients))
  print(f'all ingr {all_ingredients}')
  print(f'all allergens {all_allergens}')

  non_allergenic_ingredients = all_ingredients.copy()
  allergenic_ingredient_candidates = defaultdict(set)
  for allergen in allergen_ingredient_sets.keys():
    candidate_ingredients = all_ingredients.copy()
    #print(f'{allergen} is in one of {candidate_ingredients}')
    for ingredient_set in allergen_ingredient_sets[allergen]:
      #print(f'intersect with {ingredient_set}')
      candidate_ingredients &= ingredient_set
      #print(f'{allergen} is in one of {candidate_ingredients}')
    print(f'{allergen} is in one of {candidate_ingredients}')
    allergenic_ingredient_candidates[allergen] = candidate_ingredients
    non_allergenic_ingredients -= candidate_ingredients
  print(f'non allergenic {non_allergenic_ingredients}')
  count = 0
  for food in foods:
    for ingredient in food[0]:
      if ingredient in non_allergenic_ingredients:
        count += 1
  print(count)
  allergenic_ingredients = {}
  while len(allergenic_ingredients) < len(allergenic_ingredient_candidates):
    found = set()
    for allergen, candidate_ingredients in allergenic_ingredient_candidates.items():
      if len(candidate_ingredients) == 1:
        ingr = list(candidate_ingredients)[0]
        found.add(ingr)
        allergenic_ingredients[allergen] = ingr
    for candidate_ingredients in allergenic_ingredient_candidates.values():
      candidate_ingredients -= found
  for allergen in sorted(all_allergens):
    print(f'{allergen}: {allergenic_ingredients[allergen]}')
  print(','.join([allergenic_ingredients[allergen] for allergen in sorted(all_allergens)]))

  
    
    

if __name__ == "__main__":
    main()