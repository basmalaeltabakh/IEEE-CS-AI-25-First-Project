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
    #print(" " * 10 + " 6. Load Book from file")
    #print(" " * 10 + " 7. Save Book to file")
    print(" " * 10 + " 8. Exit") 
    print("="*50)

def main():
    library = Library()

    while True:
        showMenu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print(" Invalid choice! Please enter a number.")
            continue  

        if choice == 1:
            library.addBook()
            continue  
        
        elif choice == 2:
            library.viewBook()
            continue  
        
        elif choice == 3:
            library.searchBook()
            continue  
        
        elif choice == 4:
            bookId = input("Enter Book ID to update: ")
            newTitle = input("Enter new title (or press Enter to skip): ")
            newAuthor = input("Enter new author (or press Enter to skip): ")  
            newYear = input("Enter new publication year (or press Enter to skip): ")

            library.updateBook(bookId, 
                               newTitle=newTitle if newTitle else None, 
                               newAuthor=newAuthor if newAuthor else None, 
                               newYear=newYear if newYear else None)
            continue  
        
        elif choice == 5:
            bookId = input("Enter Book ID to delete: ")
            library.deleteBook(bookId)
            continue  
        #elif choice == 6:
           # library.loadFromFile()
            #continue  

        #elif choice == 7:
            #library.saveToFile()
           # continue  

        elif choice == 9:  
            print("Exiting Library Management System.")
            break  

        else:
            print("Invalid choice! Please enter a number between 1 and 9.")
            continue  

if __name__ == "__main__":
    main()
