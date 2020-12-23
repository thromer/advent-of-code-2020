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
  def __init__(self, id, text):
    self.id = id
    self.text = text

class FixedTile:
  def __init__(self, tile, rotation, mirror):
    self.tile = tile
    self.rotation = rotation
    self.mirror = mirror
    self.codes = {
      (-1, 0): 0,
      (0, 1): 0,
      (1, 0): 0,
      (0, -1): 0,
    }
  
class TileCollection:
  def __init__(self):
    self.all_tiles = []
    # (1, 0)[C] has fixed tiles with left code C so that
    # they will fit in pos x+1,y+0 with tile at pos x,y and right code C
    # we use (-1, 0) and (0, -1) for checking borders
    self.code_maps = {
      (1, 0): {},
      (0, 1): {}
    }
    self.all_fixed_tiles = []
  def add_tile(self, tile):
    self.all_tiles.append(tile)
    # for each of the 8 orientations,
    #  make a fixed tile
    #  compute left code and add to that map
    #  compute bottom code and add to that map
    #  etc.

class Grid:
  def __init__(self, size):
    self.size = size
    self.all_used_tiles = {}
    self.grid = {}  # position -> fixed_tile
    self.next = (0, 0)



# map is { 'map' -> {(x,y) -> FixedTile, 'next' -> (x, y) }
# tiles is 
def search(grid, tile_collection): 
  if grid.next == (0, 0):
    candidates = tile_collection.all_fixed_tiles
  else:
    # see what neighbors are already placed
    x, y = grid.next
    candidates = None
    for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
      if (x+dx, y+dy) in grid.grid:
        if dx > 0 or dy > 0:
          raise ValueError('confusion')
        neighbor = grid.grid[(x+dx, y+dy)]
        edge_code = neighbor.codes[(-dx, -dy)]
        new_candidates = tile_collection.code_maps[(-dx, -dy)]
        if candidates == None
          candidates |= new_candidates
        else:
          candidates &= new_candidates
    # filter stuff we've already used. this is pretty clunky!
    candidates = [c for c in candidates if c.tile not in grid.all_used_tiles]
    # filter by edge, if we're on the edge
    edge_dirs = []
    if x == 0:
      edge_dirs.append(-1, 0)
    if x == grid.size - 1:
      edge_dirs.append(1, 0)
    if y == 0:
      edge_dirs.append(0, -1)
    if y == grid.size - 1:
      edge_dirs.append(0, 1)
    TODO
    
      



  # consider existing # tile(s) neighboring of 'next'
  # figure out the relevant edge code
  # look up those (tile,rotation,mirror)
  # intersect (if their were two existing neighbors)
  # for each of those:
  #  determine orientation(s)
  #  copy map and tiles, update, recurse
  # missing tidbits -- must fit with all existing neighbors and with any borders

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