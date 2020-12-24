#!/usr/bin/env python3

import re
import sys

ok = 0
for line in sys.stdin:
    m = re.match(r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$', line.rstrip())
    low, high, letter, password = int(m[1]), int(m[2]), m[3], m[4]
    if len(password) < high:
        print('very bad password ', low, high, letter, password)
    else:
        n = 0
        if password[low-1] == letter:
            n += 1
        if password[high-1] == letter:
            n += 1
        if n == 1:
            ok += 1
print(ok)

        
    
