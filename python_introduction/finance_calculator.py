monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
savings = monthly_income - monthly_expenses
projected_savings = savings * 12 + savings * 12 * 0.05

print("Your monthly savings are $", savings)
print("Projected savings after one year, with interest, is: $", projected_savings)
