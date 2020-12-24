#!/usr/bin/env python3

import re
import sys

def istree(map, x, y):
    width = len(map[y])
    if width != len(map[0]):
        print('bad map!')
    return map[y][x % width] == '#'
    

map=[]
for line in sys.stdin:
    map.append(line.rstrip())
height = len(map)
print(height)
print(len(map[0]))

def countem(dx, dy):
    ntrees=0
    x=0
    y=0
    while y < height:
        if istree(map, x, y):
            print('X', x, y)
            ntrees += 1
        else:
            print('O', x, y)
        x += dx
        y += dy
    return ntrees

final=1
for dx,dy in ([1,1], [3,1], [5,1], [7,1], [1,2]):
    answer = countem(dx,dy)
    print('answer', dx,dy,answer)
    final *= answer
print(final)


        
    
