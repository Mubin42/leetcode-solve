"""
1768. Merge Strings Alternately
Link: https://leetcode.com/problems/merge-strings-alternately/description/
Status: Unsolved
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        string = ""

        i = 0
        while i < len(word1) + len(word2) + 1:
            if i % 2 == 0:
                if p1 < len(word1):
                    string += word1[p1]
                else:
                    string += " "
                p1 += 1

            elif i % 2 != 0:
                if p2 < len(word2):
                    string += word2[p2]
                else:
                    string += " "
                p2 += 1

            i += 1

        return string


if __name__ == '__main__':
    sol = Solution()
    # w1 = "abc"
    # w2 = "pqr"
    w1 = "ab"
    w2 = "pqrs"
    result = sol.mergeAlternately(w1, w2)
    print(result)
