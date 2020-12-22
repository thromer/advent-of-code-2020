#!/home/tromer/advent-of-code-2020/venv/bin/python3

# could generalize dimensions but let's not

from collections import defaultdict
from itertools import product

import re
import sys

def play_game(decks, depth):
  history = set()
  def play_round(decks):
      """returns winner"""
      decks = [list(d) for d in decks]
      cards = [decks[0][0], decks[1][0]]
      if cards[0] > len(decks[0])-1 or cards[1] > len(decks[1])-1:
        return 0 if cards[0] > cards[1] else 1
      return play_game((tuple(decks[0][1:cards[0]+1]), tuple(decks[1][1:cards[1]+1])), depth+1)
      
  decks=[list(d) for d in decks]
  while len(decks[0]) > 0 and len(decks[1]) > 0:
      decks_tuple=(tuple(decks[0]), tuple(decks[1]))
      if decks_tuple in history:
        return 0
      history.add(decks_tuple)
      winner = play_round(decks)
      decks[winner] += [decks[winner].pop(0), decks[1-winner].pop(0)]
      #for i in range(2):
        #print(i+1)
        #print(', '.join(decks[i]))
        #print("Player %d's deck: %s" % (i+1, ', '.join([str(x) for x in decks[i]])))
  score = 0
  for i in range(len(decks[winner])):
    score += (len(decks[winner]) - i) * decks[winner][i]
  print('depth=',depth,'score=',score)
  return winner

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
  play_game(decks, 1)

if __name__ == "__main__":
    main()