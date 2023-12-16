import unittest
from code import Solution


class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.s1 = Solution()

    def test_first_case(self):
        result = self.s1.romanToInt("III")
        self.assertEqual(result, 3)

    def test_second_case(self):
        result = self.s1.romanToInt("LVIII")
        self.assertEqual(result, 58)

    def test_third_case(self):
        result = self.s1.romanToInt("MCMXCIV")
        self.assertEqual(result, 1994)


if __name__ == '__main__':
    unittest.main()
