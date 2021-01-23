#!/home/ted/advent-of-code/venv/bin/python3

import functools
import re
import sys

from collections import defaultdict


def main():
    number_list = []
    for line in sys.stdin:
        n = int(line.rstrip())
        number_list.append(n)
    number_list.append(0)
    number_list.sort()
    number_list.append(number_list[-1] + 3)
    counts = defaultdict(int)
    for i in range(0, len(number_list)-1):
        counts[number_list[i+1]-number_list[i]] += 1
    print(counts)
    print(counts[1] * counts[3])


main()

    
    

