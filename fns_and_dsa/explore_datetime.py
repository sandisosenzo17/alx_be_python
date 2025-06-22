from datetime import datetime, timedelta


def display_current_datetime():
  current_date = datetime.now()
  
  #Date and time format is YYYY-MM-DD HH:MM:SS
  print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")


display_current_datetime()

num_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
  future_date = datetime.now() + timedelta(days=num_days)
  print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

calculate_future_date()