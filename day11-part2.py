#!/home/ted/advent-of-code/venv/bin/python3

# import functools
# import igraph
# import re
import sys

# from collections import defaultdict

class Grid:
    def __init__(self, grid):
        self.height = len(grid) + 2
        self.width = len(grid[0]) + 2
        blank_row = ['.'] * (self.width)
        self.grid = [blank_row]
        for row in grid:
            self.grid.append(['.'] + row + ['.'])
        self.grid.append(blank_row)

    # why isn't invert used ... ?
    def count_neighbor_states(self, x, y, state, invert):
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                visible_state = '.'
                nx = x
                ny = y
                while True:
                    nx += dx
                    ny += dy
                    if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
                        break
                    visible_state = self.grid[ny][nx]
                    if visible_state != '.':
                        break
                # change me!
                if visible_state == state:
                    count += 1
        # print('cns',x,y,state,invert,'=>',count)
        return count
    def copy_grid(self):
        result = []
        for row in self.grid:
            result.append([x for x in row])
        return result
    def advance(self):
        changed = False
        new_grid = self.copy_grid()
        for x in range(1, self.width-1):
            for y in range(1, self.height-1):
                state = self.grid[y][x]
                if (state == 'L' and 
                    self.count_neighbor_states(x, y, '#', True) == 0):
                    new_grid[y][x] = '#'
                    changed = True
                if (state == '#' and 
                    self.count_neighbor_states(x, y, '#', False) >= 5):
                    new_grid[y][x] = 'L'
                    changed = True
        self.grid = new_grid
        return changed
    def count_occupied(self):
        o = 0
        for row in self.grid:
            for cell in row:
                if cell == '#':
                    o += 1
        return o
    def display(self):
        for row in self.grid:
            print(''.join(row))
        
    
def main():
    g = []
    for line in sys.stdin:
        g.append([x for x in line.rstrip()])
    grid = Grid(g)
    # grid.display() ; print()
    while True:
        if not grid.advance():
            break
        # grid.display() ; print()
    print(grid.count_occupied())

main() 

    
    

