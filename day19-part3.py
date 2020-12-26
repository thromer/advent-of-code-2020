#!/usr/bin/env python3

import re
import sys

"""
changes
0 -> 8 11
8 -> 42
11 -> 42 31

we have
0 -> 8 11
8 -> 42 | 42 8
11 -> 42 31 | 42 11 31

seems like
- start with 1-infinity 42s (0-infinity from 8, 1 from 11)
- end with 1-infinity 31s
instead of just 1 of each
"""

class Rules:
  def __init__(self):
    self.rules = {}

  def add_rule_str(self, rule_str):
    id, body_str = re.search(r'^([0-9]+): (.*)$', rule_str).groups()
    if body_str.find('"') >= 0:
      self.rules[id] = body_str.replace('"','')
      return
    alt_strs = [x.strip() for x in body_str.split('|')]
    self.rules[id] = [[x.strip() for x in alt.split(' ')] for alt in alt_strs]

  def expand_rule(self, rule_id):
    # print(f'expand_rule({rule_id}) type={type(rule_id)}')
    rule = self.rules[rule_id]
    if type(rule) == str:
      return rule
    expanded_alts = []
    for alt in rule:
      expanded_alt = ""
      for piece in alt:
        expanded_alt += self.expand_rule(piece)
      expanded_alts.append(expanded_alt)
    mostly = ('|'.join(expanded_alts))
    # really should prepend ?: and not group singletons
    # return ('(?:' + mostly + ')') if len(expanded_alts) > 1 else mostly
    return '(' + mostly + ')'

def main():
  state = 0
  rules = Rules()
  messages = []
  for line in sys.stdin:
    line = line.strip()
    if state == 0:
      if line == '':
        state = 1
        continue
      rules.add_rule_str(line)
      continue
    if state == 1:
      messages.append(line)
      continue
    raise ValueError(f'state={state}')
  # print(rules.rules)
  regex = rules.expand_rule('0')
  print(regex)

  regex2 = (rules.expand_rule('42') + '+' +
            rules.expand_rule('31') + '+')
  print(regex2)

  count = 0
  for message in messages:
    good = re.search('^' + regex + '$', message)
    count += 1 if good else 0
    #if good:
    #  print(message)
  print(count)
  
  count2 = 0
  for message in messages:
    good = re.search('^' + regex2 + '$', message)
    count2 += 1 if good else 0
    #if good:
    #  print(message)
  print(count2)
    

if __name__ == "__main__":
    main()
