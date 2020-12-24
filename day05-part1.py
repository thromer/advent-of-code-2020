#!/usr/bin/env python3

import re
import sys

maximum = -1
for a in sys.stdin:
    a = a.rstrip()
    row = int(a[0:7].replace('F','0').replace('B', '1'),2)
    column = int(a[7:10].replace('L','0').replace('R', '1'),2)
    id = row * 8 + column
    print(id)
    if id > maximum:
        maximum = id
print(maximum)
