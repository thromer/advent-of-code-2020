#!/usr/bin/env python3

# from this we learn that we don't have to try as hard as we thought!
# basically we can pick a corner tile and then there is only one possible
# solution

# even better for part a anyway we can find the corners a priori i think (?)
# for 12x12 puzzle there are 96 borders with no mates

# so the pieces that contain those are the corners

import re
import sys

from collections import defaultdict

# co-ordinates: x, y
# normal cartesian orientation

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
  def display(self):
    return '\n'.join([f'Tile {self.id}:']+self.text)

Tile.__repr__ = Tile.display
Tile.__str__ = Tile.display
    

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
  
def main():
  tiles = []
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
        tiles.append(Tile(id, text))
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
  border_counts = defaultdict(int)
  for tile in tiles:
    for b in tile.all_borders():
      border_counts[b] += 1
  edge_borders = set([b for b in border_counts.keys() if border_counts[b] == 1])
  corners = []
  corner_product = 1
  for tile in tiles:
    if len(edge_borders & set(tile.all_borders())) == 4:
      corners.append(tile.id)
      corner_product *= tile.id
  print(corners)
  print(corner_product)
  
      
if  __name__ == "__main__":
    main()
