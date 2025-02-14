from Book import Book
import json
import os
import numpy as np


class Library:
    changes = False
    @classmethod
    def loadBooks(cls):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                return [Book(**book) for book in data]
        except FileNotFoundError:
            print("Can't find file")
            return[]
        
    def __init__(self):
        # Load books from file when the library is initialized
        self.books = Library.loadBooks()       

    # Function to add a new book
    def addBook(self):
        os.system("cls" if os.name == "nt" else "clear")
        ISBN = input("Enter Book ISBN: ").strip()
        if ISBN.lower() == "b":
            return
        

        # Check if the book ISBN already exists
        for book in self.books:
            if str(book.ISBN) == ISBN:
                print(" Invalid ISBN, Book ISBN already exists!")
                ISBN = input("Enter Valid  Book ISBN: ").strip()


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
        Id = len(self.books) + 1
        newBook = Book(Id,ISBN, title, author, int(publicationYear))
        self.books.append(newBook)
        Library.changes = True
        print(" New Book Added Successfully.")

    # Function to view books
    def viewBooks(self):
        os.system("cls" if os.name == "nt" else "clear")
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
                if optionVal.lower() == "b":                    return
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
        os.system("cls" if os.name == "nt" else "clear")
        searchTerm = input("Enter Book ISBN or Title for search (or 'b' to go back): ").strip()
        if searchTerm.lower() == "b":
            return

        for book in self.books:
            if str(book.ISBN) == searchTerm or book.title.lower() == searchTerm.lower():
                print(" Book Found!")
                book.DisplayBookDetails()
                return

        print(" Book Not Found!")

    # Function to update book details
    def updateBook(self, Id):
        os.system("cls" if os.name == "nt" else "clear")
        for book in self.books:
            if str(book.Id) == str(Id):
                print(" Book Found! Enter new details or press Enter to keep existing values.")

                newISBN = input(f"Enter new ISBN (current: {book.ISBN}): ").strip()
                if newISBN:
                    book.ISBN = newISBN

                newTitle = input(f"Enter new title (current: {book.title}): ").strip()
                if newTitle:
                    book.title = newTitle

                newAuthor = input(f"Enter new author (current: {book.author}): ").strip()
                if newAuthor:
                    book.author = newAuthor

                newPublicationYear = input(f"Enter new year (current: {book.publicationYear}): ").strip()
                if newPublicationYear.isdigit():
                    book.publicationYear = int(newPublicationYear)
                Library.changes = True
                print(" Book details updated successfully!")
                return
        
        print(" Book not found!")

    # Function to delete a book
    def deleteBook(self, Id):
        os.system("cls" if os.name == "nt" else "clear")
        for book in self.books:
            if str(book.Id) == str(Id):
                self.books.remove(book)
                print(" Book Deleted Successfully!")
                Library.changes = True
                return
        print(" Book not found!")
    
    def deleteAllBooks(self):
        os.system("cls" if os.name == "nt" else "clear")
        self.books.clear()
        print(" All Book Deleted Successfully!")
        Library.changes = True
        return
        

    
    # Function to save books to JSON file
    def saveToFile(self):
        os.system("cls" if os.name == "nt" else "clear")
        with open("data.json", "w") as file:
            json.dump([book.dictionarize() for book in self.books], file, indent=4)
        print(" Books saved successfully!")

    # Function to get Book Statistics
    def booksStatistics(self):
        os.system("cls" if os.name == "nt" else "clear")
        years = np.array([book.publicationYear for book in self.books])
        print(f"Average Publication Year: {np.mean(years)}")
        print(f"Oldest Book: {np.min(years)}")
        print(f"Newest Book: {np.max(years)}")
