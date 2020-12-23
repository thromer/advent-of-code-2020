#!/home/tromer/advent-of-code-2020/venv/bin/python3

import re
import sys

from collections import defaultdict

"""
brute force (ish) would be
1. try each tile in each of its 8 orientations in position 0, 0
2. try each remaining tile in position 0, 1
3. etc.
can optimize a bit by
- work in from the corners and edge (fewer candidates)

how long will that take? probably quadratic, not awful
could speed up a bit with a map from 'edge code' to (tile, rotation, mirror)
"""

# co-ordinates: x, y
# normal cartesian orientation

class Tile:
  pass

# map is { 'map' -> {(x,y) -> {id, rotation, mirror}, 'next' -> (x, y) }
# tiles is 
def search(map, tiles): 
  # consider existing placed tile(s) neighboring of 'next'
  # figure out the relevant edge code
  # look up those (tile,rotation,mirror)
  # intersect (if their were two existing neighbors)
  # for each of those:
  #  determine orientation(s)
  #  copy map and tiles, update, recurse

def doit():
  # for each tile
  #  for each of its 8 orientations
  #   see if it fits in position 0, 0
  #   (top and left must have no neighbors)
  #   if it does
  #     search for a solution with that map and the remaining tiles


def main():

  for line in sys.stdin:
    line = line.strip()

if __name__ == "__main__":
    main()