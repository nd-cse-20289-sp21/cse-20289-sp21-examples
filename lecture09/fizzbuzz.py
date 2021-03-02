#!/usr/bin/env python3

import os
import sys

# Functions

def fizzbuzz(start=1, stop=101):
    for number in range(start, stop):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)

# Main Execution

def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print('Usage: {} start end'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    fizzbuzz(int(args[0]), int(args[1]))

if __name__ == '__main__':
    main()
