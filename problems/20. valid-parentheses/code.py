# in this problem we have to find if the parenthesis is valid or not
# problem link: https://leetcode.com/problems/valid-parentheses/
# status: unsolved (This approach did not solve the edge cases)


class Solution:
    stack = []

    def isValid(self, s: str) -> bool:
        for item in s:
            # for left-handed items, adding to the stack
            if item == '(' or item == '{' or item == '[':
                self.stack.append(item)
            # right-handed items handling
            else:
                # is my stack is empty then return false
                if not self.stack:
                    return False
                # take out the last in the stack
                last = self.stack.pop()
                # compare it with the current item to the loop, if matches pop it, otherwise return false
                if item == '(':
                    return False
                elif item == '{' and last != '}':
                    return False
                elif item == '[' and last != ']':
                    return False
            print(self.stack)
        # if there is still items left in the stack
        if self.stack:
            return False
        return True


string = "(]"
s1 = Solution()
print(s1.isValid(string))
