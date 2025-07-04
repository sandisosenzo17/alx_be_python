class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self._is_checked_out = None

  def check_out_book(self):
    self._is_checked_out = True

  def return_book(self):
    self._is_checked_out = False

  def is_checked_out(self):
    return self._is_checked_out
  

class Library:
  def __init__(self):
    self._books = []
  
  def add_book(self, title, author):
    book = Book(title, author)
    book._is_checked_out = False
    self._books.append(book)

  def check_out_book(self, title):
    for book in self._books:
      if book.title == title:
        book.check_out_book()

  def return_book(self, title):
    for book in self._books:
      if book.title == title:
        book.return_book()
  
  def list_available_books(self):
    for book in self._books:
      if not book.is_checked_out():
        print(f"{book.title} by {book.author}")        


def main():
  library = Library()
  library.add_book("Brave New World", "Aldous Huxley")
  library.add_book("1984", "George Orwell")
  library.add_book("Physics of the impossible", "Michio Kaku")

  print("Available books after setup:")
  library.list_available_books()

  library.add_book("LOTR", "Peter Jackson")
  print("\nAvailable books after addition:")
  library.list_available_books()

  library.check_out_book("1984")
  print("\nAvailable books after checking out '1984':")
  library.list_available_books()

  library.return_book("1984")
  print("\nAvailable books after returning '1984':")
  library.list_available_books()


if __name__ == "__main__":
  main()