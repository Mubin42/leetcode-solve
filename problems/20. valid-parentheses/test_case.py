import unittest
from code import Solution


class TestValidParentheses(unittest.TestCase):

    def setUp(self):
        self.s1 = Solution()

    def test_first_case(self):
        result = self.s1.isValid("()")
        self.assertEqual(result, True)

    def test_second_case(self):
        result = self.s1.isValid("()[]{}")
        self.assertEqual(result, True)

    def test_third_case(self):
        result = self.s1.isValid("(]")
        self.assertEqual(result, False)

    def forth_test_case(self):
        result = self.s1.isValid("{[]}")
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
