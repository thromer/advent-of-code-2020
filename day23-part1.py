#!/home/tromer/advent-of-code-2020/venv/bin/python3

import re
import sys

from collections import defaultdict

MOVES = 100

def advance(cups, current):
  print(cups, current) # , type(cups), type(current))
  # first off, re-arrange so that current = 0
  cups = cups[current:] + cups[0:current]
  current = 0
  saved = cups[1:4]
  cups = [cups[0]] + cups[4:]
  destination = 9 if cups[current] == 1 else cups[current] - 1
  print(f'dest={destination}')
  while destination in saved:
    destination = 9 if destination == 1 else (destination - 1)
    print(f'dest={destination}')
  dest_index = cups.index(destination)
  cups = cups[0:dest_index+1] + saved + cups[dest_index+1:]
  current = 1
  return cups, current

def main():
  cups = [int(x) for x in sys.stdin.readline().strip()]
  current = 0
  for i in range(MOVES):
    cups, current = advance(cups, current)
  one_pos = cups.index(1)
  print(cups)
  print(''.join([str(x) for x in cups[one_pos+1:] + cups[0:one_pos]]))


if __name__ == "__main__":
    main()