#!/home/ted/advent-of-code/venv/bin/python3

# brute force ...

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
    """return halts, pc, acc"""
    pc = 0
    acc = 0
    visited = defaultdict(int)
    while True:
        print(pc, acc)
        visited[pc] += 1
        if visited[pc] == 2:
            return False, pc, acc
        if pc == len(program):
            return True, pc, acc
        pc_delta, acc_delta = execute_instruction(program[pc])
        print('delta', pc_delta, acc_delta)
        pc += pc_delta
        acc += acc_delta
    print(acc)
        
def parse_line(line):
    op, arg_str = re.match(r'^(...) (.*)$', line).groups()
    return op, int(arg_str)

def main():
    orig_program = []
    for line in sys.stdin:
        line = line.rstrip()
        orig_program.append(parse_line(line))
    for number in range(0, len(orig_program)):
        instruction = orig_program[number][0]
        if instruction == 'acc':
            continue
        test_program = [x for x in orig_program]
        new_instruction = 'nop' if instruction == 'jmp' else 'nop'
        test_program[number] = (new_instruction, orig_program[number][1])
        result = execute_program(test_program)
        if result[0]:
            print(result[2])
            break

main()
