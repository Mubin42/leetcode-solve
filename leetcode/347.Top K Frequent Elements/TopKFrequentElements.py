from collections import defaultdict
"""
347. Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/description/
Status: Unsolved
Comments:   Day - 1: Could not solve the problem.
            Day - 2: Could not solve as well.
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        hashed = defaultdict(int)

        for item in nums:
            hashed[item] += 1

        for item in list(hashed.keys()):
            if hashed[item] >= k:
                result.append(item)

        return result


if __name__ == '__main__':
    s = Solution()
    # data = [1, 1, 1, 2, 2, 3]
    # frequency = 2
    data = [1, 2]
    frequency = 2

    res = s.topKFrequent(nums=data, k=frequency)
    print(res)
