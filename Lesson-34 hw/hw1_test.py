from hw1 import NumberList
import unittest


class TestNumberList(unittest.TestCase):
    def setUp(self):
        self.my_list = NumberList([1, 3, 5, 7, 9, 11])

    # Тест на подсчёт суммы всех элементов набора:
    def test_summ_of_list(self):
        result = NumberList.sum(self.my_list)
        self.assertEqual(36, result, 'Result of the function with values: [1, 3, 5, 7, 9, 11] must be 36')

    # Тест на нахождение среднего арифметического числа из элементов набора:
    def test_average_of_list(self):
        result = NumberList.average(self.my_list)
        self.assertEqual(6, result, 'Result of the function with values: [1, 3, 5, 7, 9, 11] must be 6')

    # Тест на нахождение максимума из элементов набора:
    def test_max_of_list(self):
        result = NumberList.maximum(self.my_list)
        self.assertEqual(11, result, 'Result of the function with values: [1, 3, 5, 7, 9, 11] must be 11')

    # Тест на нахождение минимума из элементов набора:
    def test_min_of_list(self):
        result = NumberList.minimum(self.my_list)
        self.assertEqual(1, result, 'Result of the function with values: [1, 3, 5, 7, 9, 11] must be 1')


if __name__ == '__main__':
    unittest.main()