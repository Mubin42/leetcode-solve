"""
136. Single Number
Link: https://leetcode.com/problems/single-number/description/
Status: Solved
Comments:   Day - 1: Could not solve the problem.
            Day - 2: Tried a different approach and the problem is solved.
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        stack = []

        for item in nums:
            if item in stack:
                stack.remove(item)

            else:
                stack.append(item)

        return stack[0]


if __name__ == '__main__':
    s = Solution()
    data = [2, 2, 1]
    res = s.singleNumber(data)
    print(res)
