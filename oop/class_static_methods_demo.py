
class Calculator:
  calculation_type = "Arithmetic Operations"

  def __init__(self):
    pass
  
  @staticmethod
  def add(a, b):
    return a + b

  @classmethod
  def multiply(cls, a, b):
    print(f"Calculation type: {cls.calculation_type}")
    return a * b

def main():
  sum = Calculator.add(10, 5)
  print(f"The sum is: {sum}")

  product = Calculator.multiply(10, 5)
  print(f"The product is: {product}")

if __name__ == "__main__":
  main()