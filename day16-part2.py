#!/home/tromer/advent-of-code-2020/venv/bin/python3

from collections import defaultdict

import re
import sys

class Rules:
  def __init__(self):
    self.rules = {}
  def add(self, rule_str):
    field, l1, h1, l2, h2 = re.search(r'^(.*): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$', rule_str).groups()
    self.rules[field] = ((int(l1), int(h1)), (int(l2), int(h2))) 
  def valid_value(self, number):
    for ranges in self.rules.values():
      for range in ranges:
        if number >= range[0] and number <= range[1]:
          return True
    return False
  def valid_field_value(self, field, number):
    ranges = self.rules[field]
    for range in ranges:
        if number >= range[0] and number <= range[1]:
          return True
    return False
  def valid_ticket(self, numbers):
    for number in numbers:
      if not self.valid_value(number):
        return False
    return True
  def fields(self):
    return self.rules.keys()

def main():
  rules = Rules()

  for line in sys.stdin:
    line = line.rstrip()
    if line == '':
      break
    rules.add(line)
  if sys.stdin.readline().rstrip() != 'your ticket:':
    raise ValueError('hmm')
  my_ticket = [int(x) for x in sys.stdin.readline().rstrip().split(',')]
  if sys.stdin.readline().rstrip() != '':
    raise ValueError('hmm')
  if sys.stdin.readline().rstrip() != 'nearby tickets:':
    raise ValueError('hmm')
  nearby_tickets = []
  for line in sys.stdin:
    nearby_tickets.append([int(x) for x in line.rstrip().split(',')])
  #print(nearby_tickets)
  #print(rules.rules)
  bad_value_total = 0
  field_values = defaultdict(list)
  for ticket in nearby_tickets:
      if rules.valid_ticket(ticket):
        print('good ticket', ticket)
        for i in range(len(ticket)):
          field_values[i].append(ticket[i])
      else:
        print('bad ticket', ticket)
  field_names = {} # defaultdict(str)
  fields = set(rules.fields())
  for i in field_values.keys():
    field_name_candidates = set(fields)
    for val in field_values[i]:
      for field_name in fields:
        if not rules.valid_field_value(field_name, val):
          field_name_candidates.remove(field_name)
    # if len(field_name_candidates) != 1:
    #  raise ValueError(val, field_name_candidates)
    # fields -= field_name_candidates  # well this would be a nice optimization
    field_names[i] = field_name_candidates # well I'd like to be done list(field_name_candidates)[0]
  for i in sorted(field_names.keys()):
    print(sorted(field_names[i]))

  # ok this is just a hassle ...
  final_answer = {}
  while len(final_answer) < len(my_ticket):
    for i in sorted(field_names.keys()):
      if len(field_names[i]) == 1:
        found = list(field_names[i])[0]
        final_answer[i] = found
        print(final_answer)
        for s in field_names.values():
          s -= {found}
        
  print(final_answer)

  answer = 1
  for i in range(len(my_ticket)):
    if final_answer[i].find('departure ') == 0:
      answer *= my_ticket[i]
  print(answer)



if __name__ == "__main__":
    main()