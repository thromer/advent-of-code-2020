#!/home/tromer/advent-of-code-2020/venv/bin/python3

import itertools
import re
import sys

from collections import defaultdict

class Memory:
  def __init__(self):
    self.memory = defaultdict(int)
    self.mask = '0' * 36
    self.set_mask = 0
    self.float_mask = 0

  def update_mask(self, mask):
    self.mask = mask
    self.set_mask = int(mask.replace('X', '0'), base=2)
    self.float_mask = int(mask.replace('1', '0').replace('X', '1'), base=2)
  
  def store(self, address, word):
    print('store', address, word)
    address = address | self.set_mask
    float_mask_str = f'{self.float_mask:036b}'
    print('float mask str', float_mask_str)
    addr_str = f'{address:036b}'
    print('hacked addr str', addr_str)
    print(float_mask_str, addr_str)
    descriptor = ['01' if float_mask_str[i] == '1' else addr_str[i] for i in range(36)]
    print('desc',descriptor)
    for addr in itertools.product(*descriptor):
      # ugly (forgot to convert to number!)
      self.memory[addr] = word

def main():
    m = Memory()
    for line in sys.stdin:
      print(line.rstrip())
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