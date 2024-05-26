"""
Divisible Sum Pairs
Link: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true
Status: Solved
"""
from typing import List


def divisibleSumPairs(n: int, k: int, ar: List[int]) -> int:
    # Write your code here
    count = 0

    for i in range(0, n):
        for j in range(i+1, n):
            if i < j:
                total = ar[i] + ar[j]
                if total % k == 0:
                    count += 1
                    print(f"({ar[i]},{ar[j]})", end=" ")
        print()
    return count


if __name__ == '__main__':
    sample_data = [1, 3, 2, 6, 1, 2]
    length = len(sample_data)
    target = 3

    result = divisibleSumPairs(length, target, sample_data)
    print(result)
