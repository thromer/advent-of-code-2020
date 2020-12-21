#!/home/tromer/advent-of-code-2020/venv/bin/python3

import re
import sys

def preprocess_ids(ids):
  b = [ids[0]]
  d = [float('inf')]
  delta = 0
  for id in ids[1:]:
    delta += 1
    if id < float('inf'):
      b.append(id)
      d.append(delta)
      delta = 0
  return b, d

def advance(id1, id2, x1, x2):
  """Return next values of x1, x2 such that id2 * x2 > id1 * x1."""
  print('advance', id1, id2, x1, x2)
  time1 = id1 * x1
  time2 = id2 * x2
  if time1 == time2:
    raise ValueError('looping',id1,id2)
  if time1 < time2:
    x1 += int((time2-time1)/id1) + 1
    x2 += 1
  else:
    # should only happen once
    x2 += int((time1-time2)/id2) + 1
  print('result', x1, x2)
  return x1, x2

def get_answer(id1, id2, delay):
  """Return 'time' for id1 such that id2 will arrive delay minutes later."""
  # if this is too slow use binary search with upper limit determined by gcd
  # multipliers
  print('get_answer', id1, id2, delay)
  x1 = 1
  x2 = 1
  while id2 * x2 - id1 * x1 != delay:
    x1, x2 = advance(id1, id2, x1, x2)
    print(id1*x1,id2*x2)
  print('result', id1 * x1)
  return id1 * x1

def main():
    depart_time = int(sys.stdin.readline().rstrip())
    print(depart_time)
    id_strs = sys.stdin.readline().rstrip().split(',')
    print(id_strs)
    ids = [float('inf') if x == 'x' else int(x) for x in id_strs]
    print(ids)
    b, d = preprocess_ids(ids)
    print(b,d)
    answer=[b[0]]
    for i in range(1, len(b)):
      answer.append(get_answer(answer[i-1], b[i], d[i]))
    print(answer)

    sys.exit(1)

if __name__ == "__main__":
    main()