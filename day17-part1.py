#!/home/tromer/advent-of-code-2020/venv/bin/python3

from collections import defaultdict
from itertools import product

import re
import sys

class Cube:
  def __init__(self):
    self.states = defaultdict(bool)
    self.z_range = (0,0)
    self.x_range = (0,0)
    self.y_range = (0,0)
  def add_row(self, z, y, row):
    self.z_range = (min(self.z_range[0], z), max(self.z_range[1], z))
    self.y_range = (min(self.y_range[0], y), max(self.y_range[1], y))
    self.x_range = (min(self.x_range[0], 0), max(self.x_range[1], len(row)-1))
    for x in range(len(row)):
      if row[x] == '#':
        # print(x,y,z)
        self.states[(x,y,z)] = True
  def display(self):
    # print(self.x_range,self.y_range,self.z_range)
    for z in range(self.z_range[0], self.z_range[1]+1):
      print(f'z={z}')
      for y in range(self.y_range[0], self.y_range[1]+1):
        for x in range(self.x_range[0], self.x_range[1]+1):
          print('#' if self.states[(x,y,z)] else '.', end='')
        print()
  @staticmethod
  def ext(r):
    return range(r[0]-1, r[1]+2)
  def advance(self):
    updates = {}
    for x, y, z in product(self.ext(self.x_range), self.ext(self.y_range), self.ext(self.z_range)):
      # print(f'looking at {x},{y},{z}')
      active_count = 0
      for dx, dy, dz in product(*[(-1, 0, 1)]*3):
        active_count += 1 if self.states[(x+dx, y+dy, z+dz)] else 0
      if self.states[(x, y, z)]:
          if active_count != 3 and active_count != 4:
            updates[(x, y, z)] = False
      else:
          if active_count == 3: 
            updates[(x, y, z)] = True
    for key, val in updates.items():
      self.set_state(key, val)
  def set_state(self, key, val):
    x, y, z = key
    self.states[key] = val
    self.z_range = (min(self.z_range[0], z), max(self.z_range[1], z))
    self.y_range = (min(self.y_range[0], y), max(self.y_range[1], y))
    self.x_range = (min(self.x_range[0], x), max(self.x_range[1], x))
  def count_active(self):
    count = 0
    for v in self.states.values():
      count += 1 if v else 0
    return count

        

def main():
  cube = Cube()
  cube.display()
  y = 0
  for line in sys.stdin:
    line = line.rstrip()
    cube.add_row(0, y, line)
    y += 1
  cube.display()
  print()
  for i in range(6):
    print(f'After {i+1} cycles:')
    cube.advance()
    cube.display()
    print()
  print(cube.count_active())


if __name__ == "__main__":
    main()