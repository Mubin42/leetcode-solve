from collections import defaultdict
"""
215. Kth Largest Element in an Array
Link: https://leetcode.com/problems/group-anagrams/description/
Status: Solved
"""


class Solution:
    def groupAnagrams(self, strs):
        hash_map = defaultdict(list)
        result = []


        for item in strs:
            sorted_string = tuple(sorted(item))
            hash_map[sorted_string].append(item)

        for value in hash_map.values():
            result.append(value)

        return result


if __name__ == '__main__':
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = s.groupAnagrams(strs=strs)
    print(res)
