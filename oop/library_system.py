class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  def book_info(self):
    return f"Book: {self.title} by {self.author}"

class EBook(Book):
  def __init__(self, title, author, f_size):
    super().__init__(self.title, self.author)
    self.file_size = f_size

  def book_size(self):
    return self.file_size
  
  def book_info(self):
    return f"EBook {self.title} by {self.author}, File Size: {self.book_size()}"

class PrintBook(Book):
  def __init__(self, title, author, p_count):
    super().__init__(self.title, self.author)
    self.page_count = p_count
  
  def book_size(self):
    return self.page_count
  
  def book_info(self):
    return f"PrintBook {self.title} by {self.author}, Page Count: {self.book_size()}"

class Library:
  def __init__(self):
    self.books = []

  def __str__(self):
    pass

  def add_book(self, book):
    self.books.append(book)

  def list_books(self):
    for book in self.books:
      print(book.book_info())

