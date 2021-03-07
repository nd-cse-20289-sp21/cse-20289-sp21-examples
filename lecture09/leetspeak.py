#!/usr/bin/env python3

import sys

# VARIANT 1: Lists of Tuples

Mapping = [
    ('a', '4'),
    ('e', '3'),
    ('i', '1'),
    ('o', '0'),
]

'''
for line in sys.stdin:
    result = ''
    for letter in line:
        next_letter = letter
        for n, v in Mapping:
            if letter == n:
                next_letter = v
        result += next_letter
    print result
'''

# VARIANT 2: Dictionary

Mapping = {
    'a': '4',
    'e': '3',
    'i': '1',
    'o': '0',
}

for line in sys.stdin:
    result = ''
    for letter in line.rstrip():
        result += Mapping.get(letter, letter)
    print(result)
