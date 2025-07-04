import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):
  def setUp(self):
    self.calc = SimpleCalculator()
  
  def test_addition(self):
    self.assertEqual(self.calc.add(4, 7), 11)
    self.assertEqual(self.calc.add(-4, 7), 3)
    self.assertEqual(self.calc.add(4, -7), -3)
    self.assertEqual(self.calc.add(-4, -7), -11)
  
  def test_subtraction(self):
    self.assertEqual(self.calc.subtract(2, 9), -7)
    self.assertEqual(self.calc.subtract(-2, 9), -11)
    self.assertEqual(self.calc.subtract(2, -9), 11)
    self.assertEqual(self.calc.subtract(-2, -9), 7)
  
  def test_multiplication(self):
    self.assertEqual(self.calc.multiply(3, 6), 18)
    self.assertEqual(self.calc.multiply(-3, 6), -18)
    self.assertEqual(self.calc.multiply(3, -6), -18)
    self.assertEqual(self.calc.multiply(-3, -6), 18)
  
  def test_division(self):
    self.assertEqual(self.calc.divide(18, 3), 6)
    self.assertEqual(self.calc.divide(18, -3), -6)
    self.assertEqual(self.calc.divide(18, "one"), "Invalid value")
    self.assertEqual(self.calc.divide(4, 0), None)

