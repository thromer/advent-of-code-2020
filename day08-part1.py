#!/home/ted/advent-of-code/venv/bin/python3

import re
import sys

from collections import defaultdict

"""returns pc_delta, acc_delta"""
def execute_instruction(inst):
    instruction, argument = inst
    if instruction == 'nop':
        return 1, 0
    if instruction == 'acc':
        return 1, argument
    if instruction == 'jmp':
        return argument, 0
    raise ValueError
    
def execute_program(program):
    pc = 0
    acc = 0
    visited = defaultdict(int)
    while True:
        print(pc, acc)
        visited[pc] += 1
        if visited[pc] == 2:
            break
        pc_delta, acc_delta = execute_instruction(program[pc])
        print('delta', pc_delta, acc_delta)
        pc += pc_delta
        acc += acc_delta
    print(acc)
        
def parse_line(line):
    op, arg_str = re.match(r'^(...) (.*)$', line).groups()
    return op, int(arg_str)

def main():
    program = []
    for line in sys.stdin:
        line = line.rstrip()
        program.append(parse_line(line))
    execute_program(program)
    

main()
