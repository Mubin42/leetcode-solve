"""
242. Replace Elements With Greatest Element On Right Side
Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
Status: Solved
Comments:   Day - 1: Could not solve the problem.
            Day - 2: Tried Neetcode explaination video. Solved
"""


class Solution:
    def replaceElements(self, arr):
        # initial max = -1
        # reverse iteration
        # new max = max(prev, old max)
        right_max = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max

        return arr


if __name__ == '__main__':
    s = Solution()
    data = [17, 18, 5, 4, 6, 1]
    res = s.replaceElements(data)
    print(res)
