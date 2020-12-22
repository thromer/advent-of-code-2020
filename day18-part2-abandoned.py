#!/home/tromer/advent-of-code-2020/venv/bin/python3

# could generalize dimensions but let's not

from collections import defaultdict
from itertools import product

import re
import 

"""
keep track of 
- prior operands
- prior operator
- don't immediately evaluate once we have two operands
-- if next operator is higher precedence, figure out its 2nd operand
- fortunately we only have two operator so we don't need an explicit stack or tree 
- so let's say we have
- len(variables)==2
- operand=='*'
- next_operand=='+'
-- then we 
--  stash operand and v[0]
--  compute sub-expression until we get to a lower-precedence operator
that's really ugly!

3 * 5 + 6 + 7 * 8 is really
( 3 * ( ( 5 + 6 ) + 7 ) ) * 8

tree1=(3)
tree1=('*',(3),None)
something1=(5)
tree2=('+',(5),None)
something1=(6)
# '+' is not higher precedence
tree2=('+',(5),(6))
tree3=('+',('+',(5),(6)),None)
something1 = (7)
# '*' is not higher precedence
tree4=('+',('+',(5),(6)),(7))
# '*' is not higher precedence
tree1=('*',(3),('+',('+',(5),(6)),(7)))
something1 = (8)
# '*' is not higher precedence
tree5=('*',('*',(3),('+',('+',(5),(6)),(7))),None)
# 'nop' is not higher precedence
tree5=('*',('*',(3),('+',('+',(5),(6)),(7))),(8))
"""

PREC = {
  '+': 1
  '*': 0
}
class Parser:
  def get_operand(self, tokens, depth):
    # return either (number) or a tree we can evaluate later
    if tokens[0] == '(':
      return inner_do_something(tokens, depth+1)
    return (tokens.pop(0)), tokens

  def get_fancy_operand(self, tokens, prior_operator, depth):
    # consume tokens until we reach operator with lower precedence or end
    first_operand, tokens = get_operand(self, tokens, depth)
    if not tokens:
      return first_operand, tokens
    operator = tokens[0]
    if PREC[operator] < prec[prior_operator]:
      return first_operand, tokens
    # 3 + 5 + 7
    operator = tokens.pop(0)
    next_operand, tokens = get_operand(self, tokens, depth)
    # ugh    
    

  def compare_precedence(operator1, operator2):
    if operator1 == operator2:
      return 0
    if operator1 == '+' and operator2 == '*':
      return 1
    if operator1 == '*' and operator2 == '+':
      return -1
    raise ValueError('operators {operator1} {operator2}')
  
  def inner_do_something(self, tokens, depth):
    # return value, rest
    tree = None # needed?
    if tokens.pop(0) != '(':
      raise ValueError(tokens)
    if True:  # extra
      # TODO check for ')' here?
      left_operand, tokens = self.get_operand(tokens, depth)
      operator = tokens.pop(0)
      next_operand = self.get_operand(tokens, depth)
      next_token = tokens.pop(0)
      while True:
        if next_token == ')':
          return (operator, left_operand, next_operand)
        next_operator = next_token
        order = compare_precedence(operator, next_operator)
        if order >= 0:
          # e.g. '3 + 5 * 8 + 7', operator is '+' and next_operator is '*'
          # we get to consume next_operand
          left_operand = (operator, left_operand, next_operand)
          operator = next_operator
          next_operand = self.get_operand(tokens, depth)  # this just gets 8, precedence not dealt with yet
          next_token = tokens.pop(0)
        else:
          # as above but for '3 * 5 + 8 * 7'
          # and think about 3 * 5 + 8 + 9 + 10 * 7
          # left_operand 3
          # operator *
          # next_operand 5
          # next_operator +
          # want to get to
          # really at this point we want to get right_operand by consuming stuff until we land on
          # find something with precedence <= operator
          another_operand = self.get_operand(tokens, depth)
          something = (next_operator, next_operand, )
          

      


def do_something(tokens):
  # first token will be a number or a paren
  if tokens[0] != '(':
    return inner_do_something(['(']+tokens+[')'], 0)[0]
  
    

  

def test_do_something():
  do_something([3, '*', 5])


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