import math

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  return FAHRENHEIT_TO_CELSIUS_FACTOR*(fahrenheit-32)


def convert_to_fahrenheit(celsius):
  return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32

temp = input("Enter the temperature to convert: ")
temp_type = input("Is this temperature in Celsius or Fahrenheit?(C/F): ")

try:
  temp = float(temp)
  match temp_type.upper():
    case 'C':
      print(f"{temp}C is {convert_to_fahrenheit(temp)}F")
    case 'F':
      print(f"{temp}F is {convert_to_celsius(temp)}C")
    case _:
      print("Pick either C or F")
except ValueError:
  print("Please enter a number.")