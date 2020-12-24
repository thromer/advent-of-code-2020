#!/usr/bin/env python3

import re
import sys

def istree(map, x, y):
    width = len(map[y])
    return map[y][x % width] == '#'
    

map=[]
for line in sys.stdin:
    map.append(line.rstrip())
height = len(map)
dx=3
dy=1
ntrees=0
x=0
y=0
while y < height:
    if istree(map, x, y):
        ntrees += 1
    x += dx
    y += dy
print(ntrees)

        
    
