from collections import deque

"""
136. Single Number
Link: https://leetcode.com/problems/single-number/description/
Status: Unsolved
Comments: Day - 1: Could not solve the problem.
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        stack = deque()

        for item in nums:
            if item in stack:
                stack.pop()
            else:
                stack.append(item)

        print(stack)
        result = int(stack[0])
        return result


if __name__ == '__main__':
    s = Solution()
    data = [1, 0, 1]
    res = s.singleNumber(data)
    print(res)
