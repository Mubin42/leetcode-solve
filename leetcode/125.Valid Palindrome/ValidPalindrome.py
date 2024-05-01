"""
125. Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/description/
Status: Solved
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(item.lower() for item in s if item.isalnum())
        left = 0
        right = len(string) - 1

        while left < right:
            if not string[left] == string[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    sol = Solution()
    # a = "A man, a plan, a canal: Panama"
    a = '0P'
    result = sol.isPalindrome(a)
    print(result)
