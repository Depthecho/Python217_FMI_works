from calculator import Calculator
import unittest


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.a = 5
        self.b = 0

    def test_summ(self):
        result = Calculator.add(self.a, self.b)
        self.assertEqual(5, result, 'Result of the function 5 and 10 must be 5')

    def test_sub(self):
        result = Calculator.subtract(self.a, self.b)
        self.assertEqual(5, result, 'Result of the function 5 and 10 must be 5')

    def test_multiply(self):
        result = Calculator.multiply(self.a, self.b)
        self.assertEqual(0, result, 'Result of the function 5 and 10 must be 0')

    def test_divide(self):
        result = Calculator.divide(self.a, self.b)
        self.assertEqual(None, result, 'Result of the function 5 and 10 must be "None"')

    def test_maximum(self):
        result = Calculator.maximum(self.a, self.b)
        self.assertEqual(5, result, 'Result of the function 5 and 10 must be 5')

    def test_minimum(self):
        result = Calculator.minimum(self.a, self.b)
        self.assertEqual(0, result, 'Result of the function 5 and 10 must be 0')

    def test_percentage(self):
        result = Calculator.percentage(self.a, self.b)
        self.assertEqual(0, result, 'Result of the function 5 and 10 must be 0')

    def test_power(self):
        result = Calculator.power(self.a, self.b)
        self.assertEqual(1, result, 'Result of the function 5 and 10 must be 1')


if __name__ == '__main__':
    unittest.main()