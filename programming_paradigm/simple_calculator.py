class SimpleCalculator:
  def add(self, a, b):
    return a+b
  
  def subtract(self, a, b):
    return a-b
  
  def multiply(self, a, b):
    return a*b
  
  def divide(self, a, b):
    try:
      a = float(a)
      b = float(b)
    except ValueError:
      return "Invalid value"
    if b == 0:
      return None
    else:
      return a/b
