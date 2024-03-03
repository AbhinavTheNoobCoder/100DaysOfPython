#Exercise - Creating a simple library
class Library:
    def __init__(self):
        self.book_count = 0
        self.books = []

    def addBook(self, book_name):
        self.books.append(book_name)
        self.book_count += 1
    
    def searchForError(self):
        if len(self.books) != self.book_count:
            return "There is an error in your library."
        else:
            return "Everything in library is ok!"
    
library1 = Library()
library2 = Library()
library3 = Library()

while True:
    lib_no = int(input("Enter which library (1/2/3) you want to add a book to: "))
    if lib_no == 1:
        user_lib = library1
    
    elif lib_no == 2:
        user_lib = library2

    elif lib_no == 3:
        user_lib = library3
    
    else:
        print("Library not found.")
        continue
    
    print()

    book = input("Enter a book name: ")
    user_lib.addBook(book)
    
    print()

    cont = int(input("Enter 1 to continue, any other number to quit: "))
    if cont!=1:
        break

print("Searching for errors in libraries.")
print(f"Library1: {library1.searchForError()}")
print(f"Library2: {library2.searchForError()}")
print(f"Library3: {library3.searchForError()}")