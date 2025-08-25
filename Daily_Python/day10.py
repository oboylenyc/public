""" Title
Library Book Tracker

Difficulty: Intermediate

Challenge Description:
Create a Book class with the following attributes:

title (string)

author (string)

available (boolean, default True)

Add methods:

borrow(): marks the book as not available if it is currently available. If already borrowed, do nothing (or print a message).

return_book(): marks the book as available again.

__str__: returns a readable string like "The Hobbit by J.R.R. Tolkien (Available)".

Then create a small list of 3 Book objects and simulate borrowing and returning some books. """

class Book:
    def __init__(self, title: str, author: str, available: bool = True):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self) -> bool:
        """Mark as not available if possible. Return True if state changed."""
        if self.available:
            self.available = False
            return True
        return False  # already borrowed

    def return_book(self) -> bool:
        """Mark as available if possible. Return True if state changed."""
        if not self.available:
            self.available = True
            return True
        return False  # already returned

    def __str__(self) -> str:
        status = "Available" if self.available else "Not Available"
        return f"{self.title} by {self.author} ({status})"


#Testing Inputs
book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("1984", "George Orwell")
book3 = Book("Clean Code", "Robert C. Martin")

book1.borrow()
print(book1)
book1.return_book()
print(book1)

# --- Bonus: simple Library class ---
class Library:
    def __init__(self, books=None):
        self.books = list(books) if books else []

    def list_available_books(self):
        return [b for b in self.books if b.available]

    def find_book(self, title: str):
        key = title.strip().lower()
        for b in self.books:
            if b.title.lower() == key:
                return b
        return None


# Example usage of Library (optional)
library = Library([book1, book2, book3])
library.find_book("1984").borrow()
# Print all available books as strings
for b in library.list_available_books():
    print(b)