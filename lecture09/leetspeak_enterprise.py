#!/usr/bin/env python3

import sys

# Constants

MAPPING = {
    'a': '4',
    'e': '3',
    'i': '1',
    'o': '0',
}

# Functions

def translate(line):
    ''' Translates line into 1337speak 
    
    >>> translate('leet')
    'l33t'
    '''
    result = ''
    for letter in line:
        letter = MAPPING.get(letter, letter)
        result += letter
    return result

# Main Execution

def main():
    for line in sys.stdin:
        line = line.rstrip()
        print(translate(line))

if __name__ == '__main__':
    main()
