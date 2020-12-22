#!/home/tromer/advent-of-code-2020/venv/bin/python3

# probably doesn't handle the case where we can take the first bus at time 0
# probably doesn't detect loops (i.e. no answer exists)

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

def advance_no(id1, id2, x1, x2):
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



def get_answer_no(id1, id2, delay):
  """Return 'time' for id1 such that id2 will arrive delay minutes later."""
  print('get_answer', id1, id2, delay)
  x1 = 1
  x2 = 1
  while id2 * x2 - id1 * x1 != delay:
    x1, x2 = advance(id1, id2, x1, x2)
    print(id1*x1,id2*x2)
  print('result', id1 * x1)
  return id1 * x1

def advance(delta, delay, id1, id2, x1, x2):
  """Return next values of x1, x2 such that id2 * x2 + delay >= id1 * x1 + delta."""
  print('advance delta delay id1 id2 x1 x2', delta, delay, id1, id2, x1, x2)
  time1 = delta + id1 * x1
  time2 = id2 * x2
  print('time1 time2', time1, time2)
  # if time1 == time2:
  #  raise ValueError('looping?',id1,id2)
  # could batch these but oh well ... might be off by one here
  if time2 - time1 >= delay:
    x1 += max(int((time2-time1)/id1), 1)
  else:
    x2 += max(int((time1-time2)/id2), 1)
  print('result', x1, x2)
  return x1, x2

def gcd(a,b):
    if b > a:
      a, b = b, a
    while b > 0:
      a, b = b, a % b
    return a


def lcm(a,b):
    return a*b/gcd(a,b)

def get_answer(prev_answer, id2, delay):
  """Return (minimum id2*n, lcm(id1,id2)) such that id1*m + delta+delay=id2*n for some integer n,m"""
  delta, id1 = prev_answer
  print('get_answer delta id1 id2 delay',delta, id1, id2, delay)
  x1 = 1
  x2 = 1
  while (id2 * x2) - (id1 * x1 + delta) != delay:
    x1, x2 = advance(delta, delay, id1, id2, x1, x2)
    print('new candidate times', id1*x1+delta,id2*x2)
  print('result', id2 * x2)
  return id2 * x2, lcm(id1,id2)

def main():
    depart_time = int(sys.stdin.readline().rstrip())
    # print(depart_time)
    id_strs = sys.stdin.readline().rstrip().split(',')
    ids = [float('inf') if x == 'x' else int(x) for x in id_strs]
    print('ids', ids)
    b, d = preprocess_ids(ids)
    print('ids', 'delays', b,d)
    answer=[(0,b[0])]
    for i in range(1, len(b)):
      answer.append(get_answer(answer[i-1], b[i], d[i]))
    print('answer', answer)
    print('final', answer[-1][0]-len(ids)+1)

if __name__ == "__main__":
    main()