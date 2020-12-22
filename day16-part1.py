#!/home/tromer/advent-of-code-2020/venv/bin/python3

import re
import sys

class Rules:
  def __init__(self):
    self.rules = {}
  def add(self, rule_str):
    field, l1, h1, l2, h2 = re.search(r'^(.*): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$', rule_str).groups()
    self.rules[field] = ((int(l1), int(h1)), (int(l2), int(h2))) 
  def valid(self, number):
    for ranges in self.rules.values():
      for range in ranges:
        if number >= range[0] and number <= range[1]:
          return True
    return False

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
  for ticket in nearby_tickets:
    for val in ticket:
      if not rules.valid(val):
        bad_value_total += val
  print(bad_value_total)

if __name__ == "__main__":
    main()