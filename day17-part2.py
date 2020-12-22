#!/home/tromer/advent-of-code-2020/venv/bin/python3

# could generalize dimensions but let's not

from collections import defaultdict
from itertools import product

import re
import sys

class Cube:
  def __init__(self):
    self.states = defaultdict(bool)
    self.w_range = (0,0)
    self.z_range = (0,0)
    self.x_range = (0,0)
    self.y_range = (0,0)
  def add_row(self, w, z, y, row):
    self.w_range = (min(self.w_range[0], w), max(self.w_range[1], w))
    self.z_range = (min(self.z_range[0], z), max(self.z_range[1], z))
    self.y_range = (min(self.y_range[0], y), max(self.y_range[1], y))
    self.x_range = (min(self.x_range[0], 0), max(self.x_range[1], len(row)-1))
    for x in range(len(row)):
      if row[x] == '#':
        # print(x,y,z)
        self.states[(x,y,z,w)] = True
  def display(self):
    # nope
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
    for x, y, z, w in product(self.ext(self.x_range), self.ext(self.y_range), self.ext(self.z_range), self.ext(self.w_range)):
      # print(f'looking at {x},{y},{z}')
      active_count = 0
      for dx, dy, dz, dw in product(*[(-1, 0, 1)]*4):
        active_count += 1 if self.states[(x+dx, y+dy, z+dz, w+dw)] else 0
      if self.states[(x, y, z, w)]:
          if active_count != 3 and active_count != 4:
            updates[(x, y, z, w)] = False
      else:
          if active_count == 3: 
            updates[(x, y, z, w)] = True
    for key, val in updates.items():
      self.set_state(key, val)
  def set_state(self, key, val):
    x, y, z, w = key
    self.states[key] = val
    self.w_range = (min(self.w_range[0], w), max(self.w_range[1], w))
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
    cube.add_row(0, 0, y, line)
    y += 1
  #cube.display()
  #print()
  for i in range(6):
    print(f'After {i+1} cycles:')
    cube.advance()
    #cube.display()
    #print()
  print(cube.count_active())


if __name__ == "__main__":
    main()