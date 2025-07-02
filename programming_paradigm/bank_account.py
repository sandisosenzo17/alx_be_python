class BankAccount:
  def __init__(self, acc_bal=0):
    acc_bal = float(acc_bal)
    self.account_balance = acc_bal
  
  def deposit(self, amount):
    self.account_balance += amount
  
  def withdraw(self, amount):
    if self.account_balance < amount:
      return False
    else:
      self.account_balance -= amount
      return True
  
  def display_balance(self):
    print(f"Current Balance: $[{self.account_balance}]")

