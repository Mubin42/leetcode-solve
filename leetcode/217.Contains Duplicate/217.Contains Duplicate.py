"""
217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Status: Solved
"""


class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))




if __name__ == '__main__':
    res = Solution()
    data = [1, 2, 3, 1]

    result = res.containsDuplicate(data)
    print(result)
