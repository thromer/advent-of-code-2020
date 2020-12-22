#!/home/tromer/advent-of-code-2020/venv/bin/python3

# could generalize dimensions but let's not

from collections import defaultdict
from itertools import product

import re
import sys


        

def main():
  _ = sys.stdin.readline()
  decks = [[],[]]
  deck = decks[0]
  for line in sys.stdin:
    if line.rstrip() == '':
      _ = sys.stdin.readline()
      deck = decks[1]
    else:
      deck.append(int(line.rstrip()))

  while len(decks[0]) != 0 and len(decks[1]) != 0:
    cards = [decks[0].pop(0), decks[1].pop(0)]
    winner = 0 if cards[0] > cards[1] else 1
    decks[winner] += sorted(cards, reverse=True)
    print(decks)
  score = 0
  for i in range(len(decks[winner])):
    score += (len(decks[winner]) - i) * decks[winner][i]
  print(score)
  

if __name__ == "__main__":
    main()