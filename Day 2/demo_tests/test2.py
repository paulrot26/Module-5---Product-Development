import unittest
from calculator import Calculator

class TestOperation(unittest.TestCase):
    def setup(self):
        self.calc = Calculator(8,2)

    def test_sum(self):
        self.assertEqual(self.calc.get_sum(),10, "The answer was not 10.")

class TestOperation(unittest.TestCase):
    def test_subtraction(self):
        self.assertEqual(self.calc.get_subtraction(),6, "The answer was not 6.")

class TestOperation(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(self.calc.get_multiplication(),16, "The answer was not 16.")

class TestOperation(unittest.TestCase):
    def test_division(self):
        self.assertEqual(self.calc.get_division(),4, "The answer was not 4.")


if __name__ == "__main__":
    unittest.main()