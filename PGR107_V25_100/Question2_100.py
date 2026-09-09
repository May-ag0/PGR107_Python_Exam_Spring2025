#PGR107
#Kandidatnr: 100
#Question 2

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.is_checked_out = False
        
    def __str__(self):
        status = "Checked out" if self.is_checked_out else "Available"
        return f"'{self.title}' by {self.author} ({self.num_pages} pages) - {status}"
        
class Library:
    def __init__(self):
        self.books = []
        
        
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")
        
    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed from library.")
                return
        print(f"Book '{title}'not found in the library.'")

    def check_out(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_checked_out:
                    print(f"Book '{title}' is already checked out.")
                else:
                    book.is_checked_out = True
                    print(f"You have checked out '{title}'.")
                return
            print(f"Book '{title}' not found in the library.")
                
    def check_in(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_checked_out:
                    print(f"Book '{title}' is already in the library.")
                else:
                    book.is_checked_out = False
                    print(f"You have returned '{title}'.")
                    return
            print(f"Book '{title}' not found in the library.")
    
    def display_books(self):
     if not self.books:
         print("The library is empty.")
     else:
         print("Library Collection:")
         for book in self.books:
             print(book)
             
myLibrary = Library()


book1 = Book("The Girl Who Fell Beneath the Sea", "Axie Oh", 120)
book2 = Book("Book2", "Harper Lee", 180)
book3 = Book("A Court of Thorns and Roses", "Sarah J. Maas", 180)

myLibrary.add_book(book1)
myLibrary.add_book(book2)
myLibrary.add_book(book3)


myLibrary.display_books()


myLibrary.check_out("Book2")
myLibrary.check_out("Book2") 
myLibrary.check_in("Book2")
myLibrary.check_in("Book2")   

