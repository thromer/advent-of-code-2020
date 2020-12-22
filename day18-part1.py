#!/home/tromer/advent-of-code-2020/venv/bin/python3

# could generalize dimensions but let's not

from collections import defaultdict
from itertools import product

import re
import sys

def process_part(line, depth):
  "returns result of subexpr and remainder of line after ()"
  print(f'process_part({line}, {depth})')
  input = line
  token = None
  if line[0] != '(':
    raise ValueError(line)
  line = line[1:]
  result = 0
  variables = []
  op = None
  while True:
    token, line = re.search('^([0-9\+\*]+|\(|\)) ?(.*$)', line).groups()
    print(f'{depth} token={token} line={line}')
    if token == ')':
      print(f'process_part({input}, {depth})={variables[0]}')
      return variables[0], line
    if token == '(':
      subtotal, line = process_part('('+line, depth+1)
      variables.append(subtotal)
    elif token in {'*', '+'}:
      op = token
    else:
      variables.append(int(token))
    if len(variables) == 2:
      if op == '*':
        variables = [variables[0] * variables[1]]
      elif op == '+':
        variables = [variables[0] + variables[1]]
      else:
        raise ValueError('op', op)
      op = None
    print(f'op={op}, variables={variables}')
    

def process(line):
    print(f'process({line})')
    result = process_part('('+line+')', 0)[0]
    print(f'process({line})={result}')
    return result

def main():
  total = 0
  for line in sys.stdin:
    print(f'line={line}')
    total += process(line.rstrip())
  print(total)

if __name__ == "__main__":
    main()