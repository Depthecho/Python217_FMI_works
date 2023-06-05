from hw2 import Number
import unittest


class TestNumber(unittest.TestCase):
    # Тест замены числа:
    def test_set_value(self):
        num = Number(256)
        num.set_value(512)
        self.assertEqual(num.get_value(), 512)

    # Тест перевода числа в восьмеричную систему счисления:
    def test_to_octal(self):
        num = Number(256)
        self.assertEqual('0o400', num.to_octal())

    # Тест перевода числа в шестнадцатеричную систему счисления:
    def test_to_hexadecimal(self):
        num = Number(256)
        self.assertEqual('0x100', num.to_hexadecimal())

    # Тест перевода числа в двоичную систему счисления:
    def test_to_binary(self):
        num = Number(256)
        self.assertEqual('0b100000000', num.to_binary())


if __name__ == '__main__':
    unittest.main()