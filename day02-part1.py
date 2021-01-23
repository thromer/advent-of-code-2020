#!/usr/bin/env python3

import re
import sys

ok = 0
for line in sys.stdin:
    m = re.match(r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$', line.rstrip())
    low, high, letter, password = int(m[1]), int(m[2]), m[3], m[4]
    n = 0
    for c in password:
        if c == letter:
            n += 1
    if n >= low and n <= high:
        ok += 1
print(ok)

        
    
