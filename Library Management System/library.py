from book import Book
import json

class Library:

    def __init__(self):
        # Load books from file when the library is initialized
        self.books = Library.loadBooks()

    # Function to add a new book
    def addBook(self):
        Id = input("Enter Book ID: ").strip()
        if not Id.isdigit():
            print(" Invalid input! Book ID should be a number.")
            return

        # Check if the book ID already exists
        for book in self.books:
            if str(book.Id) == Id:
                print(" Invalid ID, Book ID already exists!")
                return

        # Get book details
        while True:
            title = input("Enter Book Title: ").strip()
            if title.lower() == "b":
                return
            if title.replace(" ", "").isalpha():
                break
            print(" Invalid input! Title should contain letters only.")

        while True:
            author = input("Enter Author Name: ").strip()
            if author.lower() == "b":
                return
            if author.replace(" ", "").isalpha():
                break
            print(" Invalid input! Author name should contain letters only.")

        while True:
            publicationYear = input("Enter Publication Year: ").strip()
            if publicationYear.lower() == "b":
                return
            if publicationYear.isdigit():
                break
            print(" Invalid input! Please enter a valid year.")

        # Create new book and add it to the list
        newBook = Book(int(Id), title, author, int(publicationYear))
        self.books.append(newBook)
        print(" New Book Added Successfully.")

    # Function to view books
    def viewBooks(self):
        if not self.books:
            print(" ERROR! No books available.")
            return
        
        while True:
            print("Enter 'A' to view all books, 'AU' to filter by author, 'Y' to filter by year, or 'b' to go back")
            option = input("Your choice: ").strip().upper()

            if option == "B":
                return

            if option == "AU":
                optionVal = input("Enter Author Name: ").strip()
                if optionVal.lower() == "b":
                    return
                filteredBooks = [book for book in self.books if book.author.lower() == optionVal.lower()]
            
            elif option == "Y":
                try:
                    optionVal = input("Enter Publication Year: ").strip()
                    if optionVal.lower() == "b":
                        return
                    optionVal = int(optionVal)
                    filteredBooks = [book for book in self.books if book.publicationYear == optionVal]
                except ValueError:
                    print(" Invalid input. Please enter a valid year.")
                    continue
            
            elif option == "A":
                filteredBooks = self.books
            
            else:
                print(" Invalid input! Please enter a valid choice.")
                continue

            if not filteredBooks:
                print(" No books found with the given filter.")
                return

            print(" Library Books:")
            for book in filteredBooks:
                book.DisplayBookDetails()
                print("#" * 50)

    # Function to search for a book
    def searchBook(self):
        searchTerm = input("Enter Book ID or Title for search (or 'b' to go back): ").strip()
        if searchTerm.lower() == "b":
            return

        for book in self.books:
            if str(book.Id) == searchTerm or book.title.lower() == searchTerm.lower():
                print(" Book Found!")
                book.DisplayBookDetails()
                return

        print(" Book Not Found!")

    # Function to update book details
    def updateBook(self, Id):
        for book in self.books:
            if str(book.Id) == str(Id):
                print(" Book Found! Enter new details or press Enter to keep existing values.")

                newTitle = input(f"Enter new title (current: {book.title}): ").strip()
                if newTitle:
                    book.title = newTitle

                newAuthor = input(f"Enter new author (current: {book.author}): ").strip()
                if newAuthor:
                    book.author = newAuthor

                newPublicationYear = input(f"Enter new year (current: {book.publicationYear}): ").strip()
                if newPublicationYear.isdigit():
                    book.publicationYear = int(newPublicationYear)

                print(" Book details updated successfully!")
                return
        
        print(" Book not found!")

    # Function to delete a book
    def deleteBook(self, Id):
        for book in self.books:
            if str(book.Id) == str(Id):
                self.books.remove(book)
                print(" Book Deleted Successfully!")
                return
        print(" Book not found!")

    @staticmethod
    def loadBooks():
        try:
            with open("data.json", "r") as file:
                data = json.load(file)  # Load JSON data

            
            correctedData = []
            for book in data:
                correctedData.append({
                    "Id": book.get("Id"), 
                    "title": book.get("Title", book.get("title")),  
                    "author": book.get("Author", book.get("author")), 
                    "publicationYear": book.get("publicationYear")  
                })

            return [Book(**book) for book in correctedData]

        except FileNotFoundError:
            print(" ERROR! No saved books found.")
            return []
        except json.JSONDecodeError:
            print(" ERROR! Corrupted JSON file. Resetting data.")
            return []


    # Function to save books to JSON file
    def saveToFile(self):
        with open("data.json", "w") as file:
            json.dump([book.dictionarize() for book in self.books], file, indent=4)
        print(" Books saved successfully!")