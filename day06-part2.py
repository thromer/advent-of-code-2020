#!/usr/bin/env python3

import re
import sys

def update_form(form, line):
    new_answer = set([c for c in line])
    print('new', new_answer)
    print('form', form)
    form = form.intersection(new_answer)
    print('updated', form)
    return form
        
state = 'want_form'
form = set()
forms = []
for line in sys.stdin:
    line = line.rstrip()
    if line == '':
        if state == 'have_form':
            print('answer', form, len(form), '\n\n\n')
            forms.append(form)
            state = 'want_form'
        # implicitly state want_form => want_form
        continue
    if state == 'want_form':
        form = set([c for c in line])
        state = 'have_form'
    print('call update_form')
    form = update_form(form, line)
    print('len',len(form))
if state == 'have_form':
    print('\n\n\n')
    forms.append(form)
# print(forms)
sum = 0
for form in forms:
    print(len(form))
    sum += len(form)
print(sum)

