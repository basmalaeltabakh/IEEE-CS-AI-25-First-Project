from book import Book
from library import Library


def showMenu():
    print("\n" + "="*50)
    print(" " * 10 + " Library Management System ")
    print("="*50)
    print(" " * 10 + " 1. Add Book")
    print(" " * 10 + " 2. View Books")
    print(" " * 10 + " 3. Search Book")
    print(" " * 10 + " 4. Update Book Details")  
    print(" " * 10 + " 5. Delete Book")  
    print(" " * 10 + " 6. Load Book from file")
    print(" " * 10 + " 7. Save Book to file")
    print(" " * 10 + " 8. Exit") 
    print("="*50)

def main():
    library = Library()

    while True:
        showMenu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            library.addBook()
        elif choice == "2":
            library.viewBooks()
        elif choice == "3":
            library.searchBook()
        elif choice == "4":
            library.updateBook(input("Enter Book ID to update: "))
        elif choice == "5":
            library.deleteBook(input("Enter Book ID to delete: "))
        elif choice == "6":
            library.books = Library.loadBooks()
        elif choice == "7":
            library.saveToFile()
        elif choice == "8":
            print(" Exiting Library System.")
            break
        else:
            print(" Invalid choice! Enter a number between 1-8.")


if __name__ == "__main__":
    main()