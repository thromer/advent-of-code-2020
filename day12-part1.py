#!/home/tromer/advent-of-code-2020/venv/bin/python3

import re
import sys

class Boat:

  def __init__(self):
    self.dx = 1
    self.dy = 0
    self.x = 0
    self.y = 0
    self.commands = {'F':self.f}

  def n(self, arg):
    self.y -= arg

  def s(self, arg):
    self.y += arg

  def e(self, arg):
    self.x += arg

  def w(self, arg):
    self.x -= arg

  def l(self, arg):
    if arg < 0 or arg % 90 != 0:
      raise ValueError('bad l arg %d' % arg)
    i = 0
    while i < arg:
      if self.dx > 0:
        self.dy = self.dx
        self.dx = 0
      else:
        self.dx = -self.dy
        self.dy = 0
      i += 1

  def r(self, arg):
    self.l(360-arg)
    
  def f(self, arg):
    self.x += self.dx * arg
    self.y += self.dy * arg

  def command(self, line):
    cmd, arg_str = re.search(r'^([A-Z])([0-9]+)').groups()
    arg = int(arg_str)

  def display(self):
    return 'x=%d y=%d dx=%d dy=%d' % (self.x, self.y, self.dx, self.dy)

def main():
    b = Boat()
    b.command('F90')
    print(b.display())
    sys.exit()
    print("hi there")
    for line in sys.stdin:
        b.command(line.rstrip())
    print('x',b.x,'y',b.y,'dist',abs(b.x)+abs(b.y))


if __name__ == "__main__":
    main()