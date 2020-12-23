#!/home/tromer/advent-of-code-2020/venv/bin/python3

import re
import sys

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

  def test_message_prefix(self, rule_id, message):
    """return T/F and if T, options for unmatched part of message"""
    rule = self.rules[rule_id]
    if type(rule) = str:
      if message[0] == rule:
        return True, message[1:]
      return False
    # oh but we have to consider all the possibilities?
    # well no let's take advantage of the fact that alts are always length 2?
    # no that doesn't work because rules are nested, i.e. at this level we 
    # have to return all possible suffixes ...
    result_suffixes = []
    result = False
    for alt in rule:
      if len(alt) != 2:
        raise ValueError('{rule_id}: {alt}')
      e0_result, e0_suffixes = self.test_message_prefix(elt[0], message)
      if e0_result:
        for e0_suffix in e0_suffixes:
          e1_result, e1_suffixes = self.test_message_prefix(elt[1], e0_suffix)
          if e1_result:
            result = True
            result_suffixes += e1_suffixes
    return result, result_suffixes
  
  def test_message(self, rule_id, message):
    result, suffix = self.test_message_prefix(rule_id, message):
    return result and suffix == ''

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
  print(rules.rules)
  count = 0
  for message in messages:
    good = test_message('0', message)
    count += 1 if good else 0
  print(count)
    

if __name__ == "__main__":
    main()