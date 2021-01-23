#!/usr/bin/env python3

# wow for test input we're fine until somewhere between day 70 and 80 ????

import re
import sys

from collections import defaultdict

SUBJECT_NUMBER = 7
DIVISOR = 20201227

def one_loop(n, subject_number, divisor):
  n *= subject_number
  n %= divisor
  return n
  
def get_loop_size(subject_number, public_key, divisor):
  i = 0
  n = 1
  while n != public_key:
    n = one_loop(n, subject_number, divisor)
    i += 1
    # print(i, n)
  return i
 

def main():
  card_public_key = int(sys.stdin.readline().rstrip())
  door_public_key = int(sys.stdin.readline().rstrip())
  print(f'{card_public_key=}')
  print(f'{door_public_key=}')

  # check_loop_size(loop_size, subject_number, divisor, card_public_key)
  # check_loop_size(loop_size, subject_number, divisor, card_public_key)
  
  card_loop_size = get_loop_size(SUBJECT_NUMBER, card_public_key, DIVISOR)
  door_loop_size = get_loop_size(SUBJECT_NUMBER, door_public_key, DIVISOR)
  print(f'{card_loop_size=}')
  print(f'{door_loop_size=}')
  card_n = card_public_key
  for i in range(door_loop_size-1):
    card_n = one_loop(card_n, card_public_key, DIVISOR)
    # print(f'{card_n=}')
  door_n = door_public_key
  for i in range(card_loop_size-1):
    door_n = one_loop(door_n, door_public_key, DIVISOR)
    # print(f'{door_n=}')
  if door_n != card_n:
    raise ValueError(f'{card_n=} {door_n=}')
  print(door_n)
  

if  __name__ == "__main__":
    main()
