from typing import List
"""
167. Two Sum II - Input Array Is Sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
Status: Solved
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            elif total < target:
                left += 1

        return []


if __name__ == '__main__':
    sol = Solution()
    sample = [2, 7, 11, 15]
    k = 9
    result = sol.twoSum(sample, k)

    print(result)
