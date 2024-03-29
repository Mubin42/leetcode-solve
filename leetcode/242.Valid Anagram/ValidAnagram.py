"""
242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/description/
Status: Solved
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_one = sorted(s)
        string_two = sorted(t)

        return string_one == string_two


if __name__ == '__main__':
    s = Solution()
    st1 = "anagram"
    st2 = "nagaram"
    res = s.isAnagram(st1, st2)
    print(res)