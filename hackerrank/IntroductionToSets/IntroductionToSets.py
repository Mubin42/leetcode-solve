"""
Introduction to Sets - Python (List)
Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
Status: Solved
"""


def average(array):
    # your code goes here
    array_set = set(array)

    total = 0
    for item in array_set:
        total += item

    return total / len(array_set)


if __name__ == '__main__':
    # n = int(input())
    # arr = list(map(int, input().split()))
    n = 10
    arr = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
    result = average(arr)
    print(result)
