#!/home/ted/advent-of-code/venv/bin/python3

import functools
import re
import sys

from collections import defaultdict

PREAMBLE=25


def now_find_seq(list, answer):
    for i in range(len(list)-1):
        total = list[i]
        for j in range(i+1,len(list)):
            total += list[j]
            if total > answer:
                break
            if total == answer:
                return list[i:j+1]

def main():
    number_list = []
    # number_set = set()
    for line in sys.stdin:
        n = int(line.rstrip())
        number_list.append(n)
        # number_set.add(n)
    number_set = set(number_list[:PREAMBLE])
    index = PREAMBLE
    print(number_list)
    while True:
        print('index', index)
        target = number_list[index]
        print('target ', target)
        ok = False
        for i in range(index-PREAMBLE, index):
            candidate = number_list[i]
            print('candidate ', candidate)
            want = target - candidate
            print('want ', want)
            if want != candidate and want in number_set:
                print('ok!')
                ok = True
                break
        print('tried em all')
        if not ok:
            answer = target
            break

        number_set.remove(number_list[index-PREAMBLE])
        number_set.add(target)
        index += 1

    seq = now_find_seq(number_list, answer)
    
    print(min(seq)+max(seq))

main()

    
    

