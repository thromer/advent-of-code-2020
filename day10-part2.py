#!/home/ted/advent-of-code/venv/bin/python3

import functools
import igraph
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
    number_set = set(number_list)

    edges = []
    for n in number_set:
        for m in range(n+1,n+4):
            if m in number_set:
                edges.append((n, m))
    g = igraph.Graph(directed=True, edges=edges)

    @functools.lru_cache(maxsize=None)
    def compute_path_count(source, target):
        if source == target:
            return 1
        count = 0
        for succ in [g.es[e].target for e in g.incident(source)]:
            count += compute_path_count(succ, target)
        return count

    result = compute_path_count(number_list[0], number_list[-1])
    print(result)
    
    # counts = defaultdict(int)
    # for i in range(0, len(number_list)-1):
    #    counts[number_list[i+1]-number_list[i]] += 1
    # print(counts)
    # print(counts[1] * counts[3])

    # so we have a directed graph starting from 0 and ending at max + 3
    # and perhaps there are dead ends? i don't think so

    # how do we count the number of paths
    """
    a-b\
      \ c

    so we could start with:

    a-b   1 path
    
    a-b\
     \--c   a-b-c  a-c

    1 way to get to a
    1 way to get to b
    2 ways to get to c

    if a=0 b=1 c=2 d=3 (for example)
    a-b-c-d
    a-b---d
    a---c-d
    a-----d

    2 ways to get from b to d
    1 from c to d
    1 from a to d

    and with e ... 4 from b to e
    abcde
    abc e
    ab de
    ab  e
    a cde
    a c e
    a  de
    """
main() 

    
    

