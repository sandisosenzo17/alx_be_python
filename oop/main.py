from library_system import *

def main():
  lib = Library()

  clc_book = Book("P n P", "Jane Austen")
  ebook = EBook("Snow Crash", "Neal Amstro", 600)
  pbook = PrintBook("Jack Reacher", "J.D Salibar", 342)

  lib.add_book(clc_book)
  lib.add_book(ebook)
  lib.add_book(pbook)

  lib.list_books()


if __name__ == "__main__":
  main()