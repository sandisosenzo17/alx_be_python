income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
savings = income - expenses
proj_savings = savings * 12 + savings * 12 * 0.05

print("Your monthly savings are $", savings)
print("Projected savings after one year, with interest, is: $", proj_savings)
