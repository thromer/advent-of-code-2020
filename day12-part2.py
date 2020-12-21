#!/home/tromer/advent-of-code-2020/venv/bin/python3

import re
import sys

class Boat:

  def __init__(self):
    self.dx = 1
    self.dy = 0
    self.x = 0
    self.y = 0
    self.commands = {'N': self.n, 'S': self.s, 'E': self.e, 'W': self.w,
                     'L': self.l, 'R': self.r, 'F':self.f}

  def n(self, arg):
    self.y -= arg

  def s(self, arg):
    self.y += arg

  def e(self, arg):
    self.x += arg

  def w(self, arg):
    self.x -= arg

  def r(self, arg):
    if arg < 0 or arg % 90 != 0:
      raise ValueError('bad l arg %d' % arg)
    i = 0
    # E 1,0 -> 0,1
    # S 0,1 -> -1,0
    # W -1,0 -> 0,-1
    # N 0,-1 -> 1,0
    while i < int(arg/90):
      if abs(self.dx) > 0:
        self.dy = self.dx
        self.dx = 0
      else:
        self.dx = -self.dy
        self.dy = 0
      # print(self.display())
      i += 1

  def l(self, arg):
    self.r(360-arg)
    
  def f(self, arg):
    self.x += self.dx * arg
    self.y += self.dy * arg

  def command(self, line):
    cmd, arg_str = re.search(r'^([A-Z])([0-9]+)', line).groups()
    arg = int(arg_str)
    self.commands[cmd](arg)

  def display(self):
    return 'x=%d y=%d dx=%d dy=%d' % (self.x, self.y, self.dx, self.dy)

def main():
    b = Boat()
    for line in sys.stdin:
        print(b.display())
        print(line)
        b.command(line.rstrip())
    print(b.display())
    print('x',b.x,'y',b.y,'dist',abs(b.x)+abs(b.y))


if __name__ == "__main__":
    main()