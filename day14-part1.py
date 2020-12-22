#!/home/tromer/advent-of-code-2020/venv/bin/python3

import re
import sys

from collections import defaultdict

class Memory:
  def __init__(self):
    self.memory = defaultdict(int)
    # 0 means clear, 1 means leave alone
    self.clear_mask = int('1' * 36, base=2)
    # 1 means set, 0 means leave alone
    self.set_mask = int('0' * 36, base=2)

  def update_mask(self, mask):
    self.clear_mask = int(mask.replace('X', '1'), base=2)
    self.set_mask = int(mask.replace('X', '0'), base=2)
  
  def store(self, address, word):
    word = word | self.set_mask
    word = word & self.clear_mask
    self.memory[address] = word

def main():
    m = Memory()
    for line in sys.stdin:
      maybe_mask = re.match(r'^mask = ([01X]{36})$', line.rstrip())
      if maybe_mask:
        m.update_mask(maybe_mask[1])
      else:
        address, word = re.match(r'^mem\[([0-9]+)\] = ([0-9]+)$', line.rstrip()).groups()
        m.store(int(address), int(word))
    
    # print(m.memory)
    print(sum(m.memory.values()))

if __name__ == "__main__":
    main()