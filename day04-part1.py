#!/usr/bin/env python3

import re
import sys

"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

req_fieds = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
#    'cid',
]

def update_passport(passport, line):
    for k,v in [kv.split(':') for kv in line.split(' ')]:
        passport[k] = v

def isvalid(passport):
    for k in req_fieds:
        if not k in passport:
            return False
    return True
    

state = 'want_passport'
# passport = {}
passports = []
for line in sys.stdin:
    line = line.rstrip()
    if line == '':
        if state == 'have_passport':
            passports.append(passport)
            state = 'want_passport'
        # implicitly state want_passport => want_passport
        continue
    if state == 'want_passport':
        passport = {}
        state = 'have_passport'
    update_passport(passport, line)
if state == 'have_passport':
    passports.append(passport)
# print(passports)
        

n = 0
for passport in passports:
    valid = isvalid(passport)
    if valid:
        n += 1
print(n)

