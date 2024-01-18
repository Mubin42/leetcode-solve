# problem link: https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
# status: solved
import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    li = list(s.split(' '))
    for i in range(len(li)):
        if li[i]:
            char = li[i][0]
            char = char.upper()
            li[i] = li[i].replace(li[i][0], char, 1)
        else:
            pass

    answer = ' '.join(item for item in li)
    return answer


if __name__ == '__main__':
    result = solve("chris alan")

    print(result)

