
def safe_divide(numerator, denominator):
  try:
    #Cast values appropriately
    try:
      numerator = float(numerator)
      denominator = float(denominator)
    except ValueError:
      return "Error: Please enter numeric values only."
    
    #Ensure division by zero is prohibited
    if denominator == 0:
      raise ZeroDivisionError
    else:
      return f"The result of the division is {numerator/denominator}"
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."
  
  
  