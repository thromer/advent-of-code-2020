#!/usr/bin/env python3

import re
import sys

from collections import defaultdict

deltas = {
  'w': (-2, 0),
  'e': (2, 0),
  'se': (1, -1),
  'ne': (1, 1),
  'sw': (-1, -1),
  'nw': (-1, 1),
  }

matcher = '|'.join(deltas.keys())
regexp = r'^(' + matcher+ r')(.*)$'

def find_tile(line):
  print(line)
  print(regexp)
  pos = [0, 0]
  while line:
    dir, line = re.search(regexp, line).groups()
    print(dir, line)
    delta = deltas[dir]
    pos = [pos[i] + delta[i] for i in range(2)]
  return (pos[0], pos[1])

def main():
  flipped_tiles = defaultdict(int)
  for line in sys.stdin:
    line = line.strip()
    flipped_tiles[find_tile(line)] += 1
  flipped_count = 0
  for count in flipped_tiles.values():
    if count % 2 == 1:
      flipped_count += 1
  print(flipped_count)
    
  
    

def unused_was_testing():
  new_puzzle = puzzle.clone()
  print(puzzle)
  for i in range(4):
    new_puzzle = new_puzzle.rotate()
    print()
    print(new_puzzle)
  if puzzle.text != new_puzzle.text:
    raise ValueError()

  for i in range(2):
    new_puzzle = new_puzzle.flip()
    print()
    print(new_puzzle)
  
  if puzzle.text != new_puzzle.text:
    raise ValueError()
      
if  __name__ == "__main__":
    main()
