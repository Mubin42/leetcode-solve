"""
20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/description/
Status: Solved
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for item in s:
            if item in closeToOpen.keys():
                if stack and stack[-1] == closeToOpen[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)

        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    par = "()[]{}"
    # par = "["
    result = s.isValid(par)

    print(result)