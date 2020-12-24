#!/home/ted/advent-of-code/venv/bin/python3

import re
import sys

from collections import defaultdict

PREAMBLE=25


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
            print('answer', target)
            break

        number_set.remove(number_list[index-PREAMBLE])
        number_set.add(target)
        index += 1

main()

    
    

