#!/usr/bin/env python3

import re
import sys

from collections import defaultdict

# co-ordinates: x, y
# normal cartesian orientation

MONSTER_RE = [
  r'..................#.',
  r'#....##....##....###',
  r'.#..#..#..#..#..#...',
]
MONSTER_LEN = len(MONSTER_RE[0])

class Puzzle:
  def __init__(self, text):
    self.text = text
  def rotate(self):
    new_text = []
    for i in range(len(self.text[0])):
      new_text.append(''.join([line[i] for line in self.text[::-1]]))
    return Puzzle(new_text)
  def flip(self):
    new_text = []
    for line in self.text:
      new_text.append(line[::-1])
    return Puzzle(new_text)
  def clone(self):
    return Puzzle(self.text)
  def __str__(self):
    return '\n'.join(self.text)
  def find_monsters(self):
    # check the middle row first
    # allow arbitrary overlap
    monster_count = 0
    for y in range(1, len(self.text)-1):
      row = self.text[y]
      # print(f'how about {row}')
      for x in range(0, len(row)):
        if (re.fullmatch(MONSTER_RE[1], row[x:x+MONSTER_LEN]) and
            re.fullmatch(MONSTER_RE[0], self.text[y-1][x:x+MONSTER_LEN]) and
            re.fullmatch(MONSTER_RE[2], self.text[y+1][x:x+MONSTER_LEN])):
          monster_count += 1
    return monster_count
      

def main():
  text = []
  for line in sys.stdin:
    line = line.strip()
    text.append(line)
  puzzle = Puzzle(text)
  monster_count = 0
  for i in range(2):
    puzzle = puzzle.flip()
    for j in range(4):
      puzzle = puzzle.rotate()
      count = puzzle.find_monsters()
      monster_count = max(monster_count, count)
  hash_count = 0
  for line in text:
    for c in line:
      if c == '#':
        hash_count += 1
  monster_hash_count = 0
  for line in MONSTER_RE:
    for c in line:
      if c == '#':
        monster_hash_count += 1
  rough_water = hash_count - monster_count * monster_hash_count
  print(f'{hash_count=} {monster_count=} {monster_hash_count=} {rough_water=}')
    
      
  

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
