#!/usr/bin/env python3

import re
import sys

maximum = -1
ids=[]
id_set=set()
for a in sys.stdin:
    a = a.rstrip()
    row = int(a[0:7].replace('F','0').replace('B', '1'),2)
    column = int(a[7:10].replace('L','0').replace('R', '1'),2)
    id = row * 8 + column
    ids.append(id)
    if id > maximum:
        maximum = id
ids.sort()
id_set=set(ids)
print(ids)
last=-1
for id in ids:
    if not id+1 in id_set and id+2 in id_set:
        print(id+1)

        
