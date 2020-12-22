#!/home/tromer/advent-of-code-2020/venv/bin/python3

import re
import sys

class Rules:
  def __init__(self):
    self.rules = {}

  def add_rule_str(self, rule_str):
    id, body_str = re.search(r'^([0-9]+): (.*)$', rule_str).groups()
    if body_str.find('"') >= 0:
      rules[id] = body_str.replace('"','')
      return
    alt_strs = [x.strip() for x in body.split('|')]
    rules[id] = [[x.strip() for x in alt.split(' ')] for alt in alt_strs]

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
  
    

if __name__ == "__main__":
    main()