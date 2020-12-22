#!/home/tromer/advent-of-code-2020/venv/bin/python3

import sys

from collections import defaultdict

# we'll store: recent, age

def main():
    line = sys.stdin.readline().rstrip()
    starting = [int(x) for x in line.split(',')]
    # print(starting)
    data = defaultdict(lambda: (0, 0))
    i = 1
    for last in starting:
      data[last] = i, 0
      print(i, last)
      i += 1
    while i <= 2020:
      recent, age = data[last]
      print('recent age', recent, age)
      last = 0 if age == 0 else age
      print(i, last)
      data[last] = i, i - data[last][0] if last in data else 0
      i += 1
    print(last)

if __name__ == "__main__":
    main()