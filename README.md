# Library Management System

## Project Overview
This is a simple **Library Management System** written in Python that allows users to manage books. The system provides functionality to:
- Add new books
- View all books or filter them by author/year
- Search for books by ID or title
- Update book details
- Delete books
- Save and load books from a JSON file
- View Books Statistics
- Delete All Books

The project is organized into three separate files:
1. `book.py` - Defines the `Book` class.
2. `library.py` - Implements the `Library` class, which manages the books.
3. `main.py` - The main program where the user interacts with the system.

---
## Files

### 1. `book.py`
This file defines the `Book` class, which represents a book in the library. Each book has:
- `ISBN` (string) - Unique book identifier
- `title` (string) - Title of the book
- `author` (string) - Author's name
- `publicationYear` (integer) - Year of publication

#### Functions in `book.py`
- `DisplayBookDetails()`: Prints the book details.
- `dictionarize()`: Converts the book data into a dictionary format for JSON storage.

### 2. `library.py`
This file defines the `Library` class, which manages a collection of books. It loads books from a file on initialization.

#### Functions in `library.py`
- `addBook()`: Allows the user to add a new book after validating input.
- `viewBooks()`: Displays all books or filters them by author/year.
- `searchBook()`: Searches for a book by ID or title.
- `updateBook(Id)`: Updates the details of an existing book.
- `deleteBook(Id)`: Deletes a book by its ID.
- `saveToFile()`: Saves all books to a JSON file (`data.json`).
- `loadBooks()`: Loads books from `data.json`.
- `deleteAllBooks`: Deletes all books by `clear` Function.
- `View Books Statistics()`: Displays statistics about the books in the library, such as the total number of books and other relevant data.


### 3. `main.py`
This is the entry point of the program where the user interacts with the system.

#### How `main.py` Works:
1. The program initializes a `Library` object.
2. It displays a menu with options to perform various operations.
3. The user selects an option, and the corresponding function from `Library` is called.
4. The program continues to run in a loop until the user chooses to exit.

#### Menu Options in `main.py`
```
1. Add Book
2. View Books
3. Search Book
4. Update Book Details
5. Delete Book
6. Save Books to File
7.View Books Statistics
8. Delete all Books
9. Exit
```
Each option calls the respective function from `Library`.

---
## Libraries Used
- **numpy**: Used to calculate book statistics by publication year.
- **os**: Used to clear the terminal screen at the beginning of each function for better user experience.

## Notes
- Books are stored in a file (`data.json`) for persistence.
- Entering 'b' in inputs allows the user to go back.
- The program validates input to prevent incorrect data entries.
---
#### This project is a great example of **Object-Oriented Programming (OOP)** in Python, showcasing the use of classes, file handling, and user interaction through a menu-driven approach.
---
## Contributors
- [Basmala Saeed](https://github.com/basmalaeltabakh)
- [Ayman Yasser](https://github.com/ayman-yasser)
- [Mohammed Adel](https://github.com/mohamed-295)


