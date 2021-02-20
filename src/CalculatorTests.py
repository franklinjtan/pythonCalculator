import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_addition_method(self):
        self.assertEqual(self.calculator.add(5, 5), 10)

    def test_results_subtraction_method(self):
        self.assertEqual(self.calculator.subtract(12, 4), 8)

    def test_results_multiplication_method(self):
        self.assertEqual(self.calculator.multiply(8, 8), 64)


if __name__ == '__main__':
    unittest.main()
