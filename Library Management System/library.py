import json
from Book import Book

class Library:

    @classmethod
    def load_from_file(cls):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                return [Book(**book) for book in data]
        except FileNotFoundError:
            print("Can't find file")
            return[]

    def __init__(self):
        self.books = Library.load_from_file()

    def add_book(self):
        while True:
                print("Enter 'b' to go back to menu ")
                title = input("Enter book title  ").strip()
                if title.lower() == "b":
                    return
                author = input("Enter author name: ").strip()
                if author.lower() == "b":
                    return
                year = input("Enter publication year: ").strip()
                if year.lower() == "b":
                    return
                try:
                    publication_year = int(year)
                except ValueError:
                    print("Invalid input. Please enter a valid year.")
                    continue
                book_id = len(self.books) + 1
                book = Book(book_id, title, author, publication_year)
                self.books.append(book)
                print("Book added successfully!")
                return


    def view_books(self):
        while True:
            if not self.books:
                print("No books available in the library.")
                return

            option = input(
                "Enter 'A' to view all books ,'AU' to view books with same author ,'Y' to view books with same publish year (or type 'b' to go back to menu)").strip().upper()


            if option == "B":
                return
            if option == "AU":
                option_val = input("Enter author name: ").strip()
                if option_val.lower() == "b":
                    return
                filtered_books = [book for book in self.books if book.author.lower() == option_val.lower()]
            elif option == "Y":
                try:
                    option_val = input("Enter publication year: ").strip()
                    if option_val.lower() == "b":
                        return
                    option_val = int(option_val)
                    filtered_books = [book for book in self.books if book.publication_year == option_val]
                except ValueError:
                    print("Invalid input. Please enter a valid year.")
                    continue
            elif option =="A":
                filtered_books=self.books
            else:
                print("Please enter a valid input ")
                continue

            if not filtered_books:
                print("No books found with the given input filter.")
                return

            print("Library Books:")
            for book in filtered_books:
                book.display_details()

    
    
    def search_book(self):
        while True:
            search = input("Enter book ID,title (or type 'b' to go back to menu): ").strip()
            if search.lower() == "b":
                return

            if not search:
                print("Please enter a valid input ")
                continue

            for book in self.books:
                if (str(book.id) == search or
                        book.title.lower() == search.lower()):
                    print("Book Found:")
                    book.display_message_box()
                    return
            print("Book not found.")

    def save_to_file(self):
        with open("data.json","w") as file:
            json.dump([book.dectionarize() for book in self.books], file, indent=4)
    
    
    