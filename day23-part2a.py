#!/home/tromer/advent-of-code-2020/venv/bin/python3

# brute force ... what's the clever way?
# https://wiki.python.org/moin/TimeComplexity ? 
# deque "adding to or removing from the middle is slower still."

# methinks this is the wrong language?

import re
import sys

from collections import deque

CUPS = 1000* 1000
MOVES = 100

class Entry:
  def __init__(self, start, len):
    self.start = start
    self.len = len
    self.next = None
    self.prev = None
  def display(self):
    if self.len == 1:
      return str(self.start)
    return f'{str(self.start)}..{str(self.start+self.len-1)}'

# for speed could keep pointers sorted? 
class AllOfIt:
  def __init__(self):
    self.starts = {}
    self.head = None
    self.tail = None
  def find_entry(self, n):
    keys = sorted(self.starts.keys())  # ugh extra sort every time ?!
    low = 0
    high = len(keys)-1
    while True:
      mid = int((low + high) / 2)
      mid_entry = self.starts[keys[mid]]
      if n >= mid_entry.start and n < mid_entry.start + mid_entry.len:
        return mid_entry
      if n < mid_entry.start:
        high = mid - 1
        continue
      low = mid + 1
  def append_entry(self, entry):
    # print(f'append({entry.display()})')
    if self.head == None:
      self.head = entry
      self.tail = entry
      entry.next = entry
      entry.prev = entry
    else:
      # come on! TODO BORKEN
      old_tail = self.tail
      old_tail_next = self.tail.next
      self.tail = entry
      entry.next = old_tail_next
      entry.prev = old_tail
      old_tail.next = entry
      entry.next.prev = entry
    self.starts[entry.start] = entry
  def remove_after(self, n, count):
    entry = self.find_entry(n)
    print(f'found entry {entry.display()}')
    # we keep prefix
    prefix_len = n - entry.start + 1
    prefix = Entry(entry.start, prefix_len)
    suffix = None
    removed_count = 0
    if entry.len > prefix_len:
      remove_len = min(count, entry.len - prefix_len)
      removed = [Entry(n + 1, remove_len)]
      removed_count = remove_len
      if entry.len > prefix_len + remove_len:
        suffix = Entry(n + 1 + remove_len, entry.len - prefix_len - remove_len)
      
    else:
      removed = []
    
    # but if we're unlucky we'll have to dig into up to 3 successors!!
    if removed_count < count:
      raise ValueError('implement spill')

    print(f'prefix {prefix.display()}')
    print(f'suffix {suffix.display() if suffix else ""}')
    print(f'removed {[x.display() for x in removed]}')
    
    # surgery. since we're excising old entry may need new head & tail
    # also need to update starts!
    if self.head == entry:
      self.head = prefix
    if self.tail == entry:
      self.tail = prefix 
    del self.starts[entry.start]
    before_entry = entry.prev
    after_entry = entry.next
    before_entry.next = prefix
    prefix.prev = before_entry
    self.starts[prefix.start] = prefix
    if suffix:
      prefix.next = suffix
      suffix.prev = prefix
      suffix.next = after_entry
      after_entry.prev = suffix
      self.starts[suffix.start] = suffix
    else:
      after_entry.prev = prefix
      prefix.next = after_entry
    return removed

  def insert_after(self, n, count):
    pass
  def display(self, reverse=False):
    if not reverse:
      result = [self.head.display()]
      curr = self.head.next
      while curr != self.head:
        result.append(curr.display())
        curr = curr.next
    else:
      result = [self.tail.display()]
      curr = self.tail.prev
      while curr != self.tail:
        result.append(curr.display())
        curr = curr.prev   
    return ', '.join(result)


def advance(cups, current):
  # print(cups, current) # , type(cups), type(current))
  # first off, re-arrange so that current = 0
  cups = cups[current:] + cups[0:current]
  current = 0
  saved = cups[1:4]
  cups = [cups[0]] + cups[4:]
  destination = 9 if cups[current] == 1 else cups[current] - 1
  # print(f'dest={destination}')
  while destination in saved:
    destination = 9 if destination == 1 else (destination - 1)
    # print(f'dest={destination}')
  print(f'dest={destination}')
  dest_index = cups.index(destination)
  cups = cups[0:dest_index+1] + saved + cups[dest_index+1:]
  current = 1
  return cups, current

def main():
  all = AllOfIt()
  cups = [int(x) for x in sys.stdin.readline().strip()]
  for cup in cups:
    all.append_entry(Entry(cup, 1))
  all.append_entry(Entry(len(cups)+1,CUPS-len(cups)))
  print(f'[{all.display()}]')
  print(f'r [{all.display(reverse=True)}]')
  all.remove_after(10, 3)
  print(f'[{all.display()}]')
  print(f'r [{all.display(reverse=True)}]') 

  return


  current = 0
  for i in range(MOVES):
    # if (i % 1000) == 999:
    # print(i+1)
    cups, current = advance(cups, current)
  one_pos = cups.index(1)
  # print(cups)
  # print(''.join([str(x) for x in cups[one_pos+1:] + cups[0:one_pos]]))
  n1 = cups[(one_pos+1)%CUPS]
  n2 = cups[(one_pos+2)%CUPS]
  print(n1)
  print(n2)
  print(n1*n2)


if __name__ == "__main__":
    main()