# in this problem we have to find if the parenthesis is valid or not
# problem link: https://leetcode.com/problems/valid-parentheses/
# status: unsolved (This approach did not solve the edge cases)

class Solution:
    stack = []

    def check_last(self) -> str:
        # checking edge cases
        return self.stack[-1] if len(self.stack) != 0 else "0"

    def isValid(self, s: str) -> bool:
        # if the items are left bracket add the items
        for item in s:
            if item == '(' or item == '{' or item == '[':
                self.stack.append(item)

            elif item == ')':
                if self.check_last() == '(':
                    self.stack.pop()
                else:
                    return False

            elif item == '}':
                if self.check_last() == '{':
                    self.stack.pop()
                else:
                    return False

            elif item == ']':
                if self.check_last() == '[':
                    self.stack.pop()
                else:
                    return False

        return len(self.stack) == 0


string = "{[]}"
s1 = Solution()
print(s1.isValid(string))
