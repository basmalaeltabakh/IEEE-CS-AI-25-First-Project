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
    print(" " * 10 + " 6. Save Book to file")
    print(" " * 10 + " 7. View Books Statistics")
    print(" " * 10 + " 8. Delete all Books")
    print(" " * 10 + " 9. Exit") 
    print("="*50)

def main():
    library = Library()

    while True:
        showMenu()
        choice = input("Enter your choice: ").strip()
        match choice:
            case "1":
                library.addBook()
            case "2":
                library.viewBooks()
            case "3":
                library.searchBook()
            case "4":
                library.updateBook(input("Enter Book ID to update: "))
            case "5":
                library.deleteBook(input("Enter Book ID to delete: "))        
            case "6":
                library.saveToFile()
            case "7":
                library.booksStatistics()
            case "8":           
                library.deleteAllBooks()
            case "9":
                if Library.changes:
                    save = input("Do you want save changes[y/n]: ").lower()
                    while save not in ["y", "n"]:
                        save = input("Do you want save changes[y/n]: ").lower()
                    if save == "y":
                        library.saveToFile()
                    
                print(" Exiting Library System.")
                break
            case _:
                print(" Invalid choice! Enter a number between 1-8.")

if __name__ == "__main__":
    main()
