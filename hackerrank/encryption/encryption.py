# in this problem we have to encode a text
# problem link: https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true
# status: unresolved

# !/bin/python3

import math
import os
import random
import re
import sys


def encryption(s) -> str:
    # Write your code here
    s.replace(' ', '')
    length = len(s)
    square_root = math.sqrt(length)

    rows = math.floor(square_root)
    columns = math.ceil(square_root)

    grid = ['' for i in range(rows)]
    index = 0
    for i in range(rows):
        for j in range(columns):
            if index < length:
                grid[i] = grid[i] + s[index]
                index += 1

    print(grid)

    encrypted = ' '.join(grid)
    return encrypted


if __name__ == '__main__':
    # Sample Input 0
    input_text_0 = "have a nice day"
    output_0 = encryption(input_text_0)
    print(output_0)
    # Output: hae and via ecy

    # Sample Input 1
    input_text_1 = "feed the dog"
    output_1 = encryption(input_text_1)
    print(output_1)
    # Output: fto ehg ee dd

    # Sample Input 2
    input_text_2 = "chill out"
    output_2 = encryption(input_text_2)
    print(output_2)
    # Output: clu hlt io
