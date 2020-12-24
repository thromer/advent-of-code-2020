#!/usr/bin/env python3

# wow for test input we're fine until somewhere between day 70 and 80 ????

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

black_tiles = set()
min_y = 0
min_x = 0
max_y = 0
max_x = 0

def find_tile(line):
#  print(line)
#  print(regexp)
  pos = [0, 0]
  while line:
    dir, line = re.search(regexp, line).groups()
#    print(dir, line)
    delta = deltas[dir]
    pos = [pos[i] + delta[i] for i in range(2)]
  return (pos[0], pos[1])

def advance():
  global black_tiles
  global min_y
  global min_x
  global max_y
  global max_x
  # print(sorted(black_tiles))
  new_black_tiles = black_tiles.copy()

  new_min_y = float('inf')
  new_min_x = float('inf')
  new_max_y = -float('inf')
  new_max_x = -float('inf')
  for x in range(min_x-2, max_x+3):
    for y in range(min_y-2, max_y+3):
      black_n_count = 0
      for delta in deltas.values():
        if (x + delta[0], y + delta[1]) in black_tiles:
          black_n_count += 1
      if (x, y) in black_tiles:
        # black
        if black_n_count == 0 or black_n_count > 2:
          new_black_tiles.remove((x, y))
      else:
        # white
        if black_n_count == 2:
          new_black_tiles.add((x, y))
          new_min_x = min(new_min_x, x)
          new_max_x = max(new_max_x, x)
          new_min_y = min(new_min_y, y)
          new_max_y = max(new_max_y, y)
  min_x = new_min_x
  max_x = new_max_x
  min_y = new_min_y
  max_y = new_max_y
  black_tiles = new_black_tiles
  

def main():
  global black_tiles
  global min_y
  global min_x
  global max_y
  global max_x
  flipped_tiles = defaultdict(int)
  for line in sys.stdin:
    line = line.strip()
    flipped_tiles[find_tile(line)] += 1
  flipped_count = 0
  for count in flipped_tiles.values():
    if count % 2 == 1:
      flipped_count += 1
  print(flipped_count)
  for tile in [k for k in flipped_tiles.keys() if flipped_tiles[k] % 2 == 1]:
    black_tiles.add(tile)
    min_x = min(min_x, tile[0])
    max_x = max(max_x, tile[0])
    min_y = min(min_y, tile[1])
    max_y = max(max_y, tile[1])

  for i in range(100):
    advance()
    print(f'Day {i+1}: {len(black_tiles)}')
  print(len(black_tiles))
  

if  __name__ == "__main__":
    main()
