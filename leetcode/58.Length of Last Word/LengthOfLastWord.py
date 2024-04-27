"""
58. Length Of Last Word
Link: https://leetcode.com/problems/length-of-last-word/description/
Status: Solved
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls = list(s.split(" "))
        filtered = []
        for item in ls:
            if item != "":
                filtered.append(item)

        return len(filtered[-1])


if __name__ == '__main__':
    s = Solution()
    text = "   fly me   to   the moon  "
    result = s.lengthOfLastWord(text)
    print(result)


