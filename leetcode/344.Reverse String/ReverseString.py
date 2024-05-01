"""
344. Reverse String
Link: https://leetcode.com/problems/reverse-string/description/
Status: Solved
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1

        print(s)


if __name__ == '__main__':
    sol = Solution()
    sample = ["h", "e", "l", "l", "o"]
    sol.reverseString(sample)
