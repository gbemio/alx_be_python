import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a new calculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_signs(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    # --- Subtraction Tests ---
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_subtraction_mixed_signs(self):
        self.assertEqual(self.calc.subtract(-5, 3), -8)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(0, 5), -5)

    # --- Multiplication Tests ---
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, -5), 20)

    def test_multiplication_mixed_signs(self):
        self.assertEqual(self.calc.multiply(-4, 5), -20)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)

    # --- Division Tests ---
    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_result_float(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_mixed_signs(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == "__main__":
    unittest.main()
