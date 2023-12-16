# convert from roman numerals to integers
# problem link = https://leetcode.com/problems/roman-to-integer/description/

# my return would be in integer
# input would be in roman string literals
class Solution(object):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # helper function
    def convert(self, character: str):
        return self.roman_dict.get(character)

    def romanToInt(self, s: str) -> int:
        total = 0
        for index, item in enumerate(s, len(s)):
            value = self.convert(item)
            total += value

        return total


if __name__ == '__main__':
    s1 = Solution()
    result = s1.romanToInt("III")
    print(result)
