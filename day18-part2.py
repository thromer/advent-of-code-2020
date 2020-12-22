#!/home/tromer/advent-of-code-2020/venv/bin/python3


import re
import sys

"""
https://www.chris-j.co.uk/parsing.php

For each token in turn in the input infix expression:
If the token is an operand, append it to the postfix output.
If the token is an operator A then:
While there is an operator B of higher or equal precidence than A at the top of the stack, 
  pop B off the stack and append it to the output.
Push A onto the stack.
If the token is an opening bracket, then push it onto the stack.
If the token is a closing bracket:
Pop operators off the stack and append them to the output, 
  until the operator at the top of the stack is a opening bracket.
Pop the opening bracket off the stack.
When all the tokens have been read:
While there are still operator tokens in the stack:
Pop the operator on the top of the stack, and append it to the output.
"""

PREC = {
  '+': 1,
  '*': 0,
}

def tokenize(line):
  result = []
  while line:
    # print(f'line=[{line}]')
    token, line = re.search('^([0-9\+\*]+|\(|\)) ?(.*$)', line).groups()
    if token in [')','('] + list(PREC.keys()):
      result.append(token)
    else:
      result.append(int(token))
  return result

def process_tokens(tokens):
    print('infix tokens=%s' % tokens)
    result = []
    stack = []
    for token in tokens:
      if type(token) == int:
        result.append(token)
        continue
      if token in PREC.keys():
        while stack and stack[-1] in PREC.keys() and PREC[stack[-1]] >= PREC[token]:
          result.append(stack.pop())
        stack.append(token)
        continue
      if token == '(':
        stack.append(token)
        continue
      if token == ')':
        while True:
          top = stack.pop()
          if top == '(':
            break
          result.append(top)
        continue
      raise ValueError(token)
    while stack:
      result.append(stack.pop())
    return result

def apply_operator(operator, op1, op2):
  if operator == '+':
    return op1 + op2
  if operator == '*':
    return op1 * op2
  raise ValueError(operator)

def evaluate_postfix(tokens):
  if not tokens:
    raise ValueError()
  print(tokens)
  stack = []
  for i in range(len(tokens)):
    # print(stack)
    if type(tokens[i]) == int:
      stack.append(tokens[i])
      continue
    if len(stack) >= 2:
      stack.append(apply_operator(tokens[i], stack.pop(), stack.pop()))
      continue
    raise ValueError(stack, i)
  if len(stack) != 1:
    raise ValueError(stack)
  return stack[0]
        
def main():
  #print(evaluate_postfix(process_tokens([3,'+',5,'*',8,'+',7])))
  #print(evaluate_postfix(process_tokens([3, '+', '(', 5, '*', 8, ')', '+', 7])))
  total = 0
  for line in sys.stdin:
    value = evaluate_postfix(process_tokens(tokenize(line.rstrip())))
    print(f'value={value}')
    total += value
  print(total)

if __name__ == "__main__":
    main()