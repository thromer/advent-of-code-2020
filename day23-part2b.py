#!/usr/bin/env python3

import re
import sys
from llist import dllist

from collections import deque

CUPS = 1000* 1000
MOVES = 10 * 1000 * 1000

class IndexedDllist:
  def __init__(self, size):
    self.index = [None] * size
    self.dll = dllist()
  def append(self,item):
    node = self.dll.append(item)
    self.index[item] = node
  def size(self):
    return self.dll.size
  def remove_right(self, target_node):
    if target_node == self.dll.last:
      result = self.dll.remove(self.dll.first)
    else:
      result = self.dll.remove(target_node.next)
    self.index[result] = None
    return result
  def first(self):
    return self.dll.first
  def __str__(self):
    return self.dll.__str__()
  def __repr__(self):
    return self.dll.__repr__()
  def insert_after(self, target_node, item):
    if target_node == self.dll.last:
      return self.append(item)
    node = self.dll.insert(item, target_node.next)
    self.index[item] = node
    return node
  def get_right(self, target_node):
    if target_node == self.dll.last:
      return self.dll.first
    return target_node.next
  
def sub1(v):
  return (v - 1) if v > 1 else CUPS

def advance(all, current):
  removed = [all.remove_right(current) for i in range(3)]
  # print(removed)
  destination = sub1(current.value)
  while destination in removed:
    destination = sub1(destination)
  dest_node = all.index[destination]
  for i in range(2, -1, -1):
    all.insert_after(dest_node, removed[i])
  return all.get_right(current)

def main():
  all = IndexedDllist(CUPS+1)
  cups = [int(x) for x in sys.stdin.readline().strip()]
  for cup in cups:
    print(f'cup={cup}')
    all.append(cup)
  print(f'[{all}]')
  for cup in range(len(cups)+1,CUPS+1):
    all.append(cup)
  # print(f'[{all}]')
  current = all.first()
  for i in range(MOVES):
    current = advance(all, current)
    if i % 1000 == 999:
      print(i+1)
    # print(i+1, current, all)
  node1 = all.index[1]
  star1_node = all.get_right(node1)
  star2_node = all.get_right(star1_node)
  print(star1_node.value)
  print(star2_node.value)
  print(star1_node.value * star2_node.value)


if __name__ == "__main__":
    main()
