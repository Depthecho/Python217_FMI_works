from fraction import Fraction
import unittest

a = Fraction(2, 2)
b = Fraction(3, 3)


class TestFraction(unittest.TestCase):

    def test_frac_summ(self):
        self.assertEqual(str(a+b), str(a + b), "Result of the function {2, 2, 3, 3} must be 12/6")

    def test_frac_sub(self):
        self.assertEqual(str(a-b), str(a - b), "Result of the function {2, 2, 3, 3} must be 0/6")

    def test_frac_mul(self):
        self.assertEqual(str(a*b), str(a * b), "Result of the function {2, 2, 3, 3} must be 6/6")

    def test_frac_truediv(self):
        self.assertEqual(str('15/7'), str(a / b), "Result of the function {2, 2, 3, 3} must be 6/6")


if __name__ == '__main__':
    unittest.main()