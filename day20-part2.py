#!/usr/bin/env python3

import re
import sys

from collections import defaultdict
from functools import reduce

"""
0. preprocess all the tiles to find their 4 edges in each of 8 'orientations'
1. pick an arbitrary corner tile in an arbitrary orientation
2. place it in 0,0
3. search for 0,1 (rotate and flip each tile)
4.  etc.
"""

# co-ordinates: x, y
# normal cartesian orientation


def rotate_text(text):
  new_text = []
  for i in range(len(text[0])):
    new_text.append(''.join([line[i] for line in text[::-1]]))
  return new_text
def flip_text(text):
  new_text = []
  for line in text:
    new_text.append(line[::-1])
  return new_text
  
class Tile:
  def __init__(self, id, text):
    self.id = id
    self.text = text
    self.edges = {}
    self.edges[False] = {
      (0, 1): text[0],
      (0, -1): text[-1],
      (-1, 0): ''.join([line[0] for line in text]),
      (1, 0): ''.join([line[-1] for line in text]),
    }
    # not really clear what the physical interpretation is here ...
    self.edges[True] = {
      k: v[::-1] for k, v in self.edges[False].items()
    }
  def all_borders(self):
    return list(self.edges[False].values()) + list(self.edges[True].values())
  def orient(self, flip, rotate):
    new_text = self.text
    for i in range(flip):
      new_text = flip_text(new_text)
    for i in range(rotate):
      new_text = rotate_text(new_text)
    return Tile(self.id, new_text)
  def __str__(self):
    return '\n'.join([f'Tile {self.id}:']+self.text)

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

FLIP_ROTATE=reduce(lambda a, b: a + b, 
                   [[(flip, rotate) for flip in range(2)]
                    for rotate in range(4)])

def get_edge_patterns(tiles):
  border_counts = defaultdict(int)
  for tile in tiles:
    for b in tile.all_borders():
      border_counts[b] += 1
  return set([b for b in border_counts.keys() if border_counts[b] == 1])

def get_corner_tiles(tiles, edge_patterns):
  corners = []
  for tile in tiles:
    if len(edge_patterns & set(tile.all_borders())) == 4:
      corners.append(tile)
  product = 1
  for t in corners:
    product *= t.id
    print(t.id)
  print(product)
  return corners

def solve_puzzle(all_tiles):
  grid_size=int(len(all_tiles)**0.5)
  grid = []
  for i in range(grid_size):
    grid.append([None]*grid_size)
  edge_patterns = get_edge_patterns(all_tiles)
  corner_tile = get_corner_tiles(all_tiles, edge_patterns)[0]
  available_tiles = all_tiles.copy()
  for flip, rotate in FLIP_ROTATE:
    fixed_tile = corner_tile.orient(flip, rotate)
    if (fixed_tile.edges[False][(-1, 0)] in edge_patterns and 
        fixed_tile.edges[False][(0, -1)] in edge_patterns):
      corner_fixed_tile = fixed_tile
      break
  print(f'x=0 y=0 id={corner_tile.id}')
  available_tiles.remove(corner_tile)
  grid[0][0] = corner_fixed_tile
  for x in range(grid_size):
    for y in range(grid_size):
      print(f'Working on {x=} {y=}')
      if grid[x][y]:
        # print(f'never mind have id={grid[x][y].id}')
        continue
      needed_borders = {}
      for deltas in (-1, 0), (0, -1):
        neighbor = (x + deltas[0], y + deltas[1])
        if grid[neighbor[0]][neighbor[1]]:
          needed_borders[deltas] = grid[neighbor[0]][neighbor[1]].edges[False][(-deltas[0], -deltas[1])]
      if len(needed_borders) == 0:
        raise ValueError('oops')
      found = None
      found_fixed = None
      for candidate in available_tiles:
        for flip, rotate in FLIP_ROTATE:
          candidate_fixed = candidate.orient(flip, rotate)
          matches = True
          for delta, needed_border in needed_borders.items():
            if candidate_fixed.edges[False][delta] != needed_border:
              matches = False
              break
          if matches:
            found = candidate
            found_fixed = candidate_fixed
            break
        if found:
          break
      # print(f'{found_fixed=}')
      # print(f'{found=}')
      
      print(f'{x=} {y=} id={found.id}')
      grid[x][y] = found_fixed
      available_tiles.remove(found)
  return grid

def print_ocean(grid):
  piece_size = len(grid[0][0].text)
  for y in range(len(grid)-1, -1, -1):
    for piece_y in range(1, piece_size-1):
      for x in range(0, len(grid)):
#        print(x, y, grid[x][y].id)
#        print(x, y, piece_y)
        # not print(f'{grid[x][y].text[piece_y]} ', end='')
        print(f'{grid[x][y].text[piece_y][1:-1]}', end='')
      print()

  for y in range(len(grid)-1, -1, -1):
    for x in range(0, len(grid)):
      print(f'{grid[x][y].id} ', end='')
    print()
    
def main():
  tiles = set()
  state = 'new_tile'
  for line in sys.stdin:
    # print(f'{state=}')
    line = line.strip()
    # print(f'line=[{line}]')
    if state == 'new_tile':
      id = int(re.search(r'^Tile (.*):$', line).groups()[0])
      # print(f'got {id=}')
      state = 'tile_line_1'
      continue
    if state == 'tile_line_1':
      text = [line]
      size = len(line)
      #print(f'set {size=}')
      state = 'tile_body'
      continue
    if state == 'tile_body':
      if len(line) != size:
        raise ValueError(f'wrong length [{line=}]')
      text.append(line)
      if len(text) == size:
        tiles.add(Tile(id, text))
        del id
        del text
        state = 'blank_line'
      continue
    if state == 'blank_line':
      if line != '':
        raise ValueError(f'expected blank line but got [{line}]')
      state = 'new_tile'
      continue
    raise ValueError(f'state {state}')
  if state != 'blank_line':
    raise ValueError(f'reached end of input but {state=}')

  grid = solve_puzzle(tiles)
  print_ocean(grid)

if __name__ == "__main__":
    main()
