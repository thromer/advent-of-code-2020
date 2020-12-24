#!/usr/bin/env python3

import re
import sys

from collections import defaultdict

# co-ordinates: x, y
# normal cartesian orientation

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
  
def main():
  text = []
  for line in sys.stdin:
    line = line.strip()
    text.append(line)
  puzzle = Puzzle(text)

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
