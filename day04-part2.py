#!/usr/bin/env python3

import re
import sys

"""
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

def check_year(year, low, high):
    try:
        y = int(year)
    except ValueError as e:
        return False
    return y >= low and y <= high

def isvalid(p):
    for k in req_fieds:
        if not k in p:
            return False
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if not (check_year(p['byr'], 1920, 2002) and
            check_year(p['iyr'], 2010, 2020) and
            check_year(p['eyr'], 2020, 2030)):
        return False
    # hgt (Height) - a number followed by either cm or in:
    m = re.match(r'^([0-9]+)(cm|in)$', p['hgt'])
    if not m:
        return False
    if m[2] == 'cm':
        # If cm, the number must be at least 150 and at most 193.
        if not check_year(m[1], 150, 193):
            return False
    else:
        # If in, the number must be at least 59 and at most 76.
        if not check_year(m[1], 59, 76):
            return False
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if not re.match(r'^#[a-f0-9]{6}$', p['hcl']):
        return False
    # ecl (Eye Color) - exactly one of these
    if p['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if not re.match(r'^[0-9]{9}$', p['pid']):
        return False
    # cid (Country ID) - ignored, missing or not.

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
    print(valid)
    if valid:
        n += 1
print(n)

