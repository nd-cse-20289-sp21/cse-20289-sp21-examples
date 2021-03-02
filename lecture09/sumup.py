#!/usr/bin/env python3

import sys

numbers = []

for argument in sys.argv[1:]:
    try:
        numbers.append(int(argument))
    except ValueError:
        pass

print(f'The sum of {numbers} is {sum(numbers)}')
