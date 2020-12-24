#!/usr/bin/env python3

import re
import sys

def update_form(form, line):
    for c in line:
        form.add(c)
        
state = 'want_form'
forms = []
for line in sys.stdin:
    line = line.rstrip()
    if line == '':
        if state == 'have_form':
            forms.append(form)
            state = 'want_form'
        # implicitly state want_form => want_form
        continue
    if state == 'want_form':
        form = set()
        state = 'have_form'
    update_form(form, line)
if state == 'have_form':
    forms.append(form)
# print(forms)
sum = 0
for form in forms:
    print(len(form))
    sum += len(form)
print(sum)

sys.exit(1)

n = 0
for form in forms:
    valid = isvalid(form)
    print(valid)
    if valid:
        n += 1
print(n)

