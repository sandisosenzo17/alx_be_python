import math

def perform_operation(num1, num2, operation):
	
	if math.isnan(num1):
		return "Please provide numbers."
	if math.isnan(num2):
		return "Please provide numbers."
	match(operation):
		case "add":
			return float(num1)+num2
		case "subtract":
			return float(num1)-num2
		case "multiply":
			return float(num1)*num2
		case "divide":
			if num2 == 0:
				return "Division by zero"
			else:
				return float(num1)/num2
		case _:
			return "Unknown operation"

