#!/home/tromer/advent-of-code-2020/venv/bin/python3

import re
import sys



def main():
    depart_time = int(sys.stdin.readline().rstrip())
    print(depart_time)
    id_strs = sys.stdin.readline().rstrip().split(',')
    print(id_strs)
    ids = [float('inf') if x == 'x' else int(x) for x in id_strs]
    print(ids)
    waits = [x - depart_time % x for x in ids]
    wait_time = min(waits)
    id = ids[waits.index(wait_time)]
    print(id * wait_time)


if __name__ == "__main__":
    main()