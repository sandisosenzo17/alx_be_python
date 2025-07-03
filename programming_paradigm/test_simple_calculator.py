import unittest
from simple_calculator import SimpleCalculator as SC

class TestCalculator(unittest.TestCase):
  def setUp(self):
    self.sc = SC()
  
  def test_addition(self):
    self.assertEqual(self.sc.add(4, 7), 11)
    self.assertEqual(self.sc.add(-4, 7), 3)
    self.assertEqual(self.sc.add(4, -7), -3)
    self.assertEqual(self.sc.add(-4, -7), -11)
  
  def test_subtraction(self):
    self.assertEqual(self.sc.subtract(2, 9), 11)
    self.assertEqual(self.sc.subtract(-2, 9), 7)
    self.assertEqual(self.sc.subtract(2, -9), -5)
    self.assertEqual(self.sc.subtract(-2, -9), -11)
  
  def test_multiply(self):
    self.assertEqual(self.sc.multiply(3, 6), 18)
    self.assertEqual(self.sc.multiply(-3, 6), -18)
    self.assertEqual(self.sc.multiply(3, -6), -18)
    self.assertEqual(self.sc.multiply(-3, -6), 18)
  
  def test_divide(self):
    self.assertEqual(self.sc.divide(18, 3), 6)
    self.assertEqual(self.sc.divide(18, -3), -6)
    self.assertEqual(self.sc.divide(18, "one"), "Invalid value")
    self.assertEqual(self.sc.divide(4, 0), None)

