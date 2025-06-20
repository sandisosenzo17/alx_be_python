shopping_list = []

def main():
  while True:
    menu()
    choice = input("Enter your choice(1, 2, 3 or 4): ")

    if choice == '1':
      add()
    elif choice == '2':
      delete()
    elif choice == '3':
      view()
    elif choice == '4':
      print("Goodbye!")
      break
    else:
      print("Invalid choice!")

def add():
  item = input("Enter item to add: ")
  shopping_list.append(item)
  print("Item added")

def delete():
  item = input("Enter item to delete: ")
  counter = 0
  for i in shopping_list:
    counter += 1
    if i == item:
      shopping_list.remove(item)
      print("Item deleted")
      break
    
    lst_length = len(shopping_list)
    if counter == lst_length and shopping_list[lst_length-1] != item:
      print("Item not found")
      break

def view():
  for i in shopping_list:
    print(i)

def menu():
  print("\t\tShopping List Manager")
  print("1. Add Item")
  print("2. Remove Item")
  print("3. View List")
  print("4. Exit")

if __name__ == "__main__":
  main()