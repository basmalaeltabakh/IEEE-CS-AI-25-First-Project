from book import Book
import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self):
        self.books = []
    
    def addBook (self):
        ID = input("Enter Book ID : ")
        for book in self.books:
            if book.id == ID:
                print("Invalid ID , Book Id already exists ! ")
                #messagebox.showerror("Error", "Book ID already exists!")
                return
        while True:
          title = input("Enter Book Title: ")
          if title.replace(" ", "").isalpha():
             break
          else:
             print("Invalid input! Title should contain letters only.")

        while True:
          author = input("Enter Author Name: ")
          if author.replace(" ", "").isalpha():
            break
          else:
             print("Invalid input! Author name should contain letters only.")

        while True:
          publicationYear = input("Enter Publication Year: ")
          if publicationYear.isdigit(): 
            break
          else:
            print(" Invalid input ! Please enter a valid year .")

        newBook = Book(ID , title , author , publicationYear)
        self.books.append(newBook)
        print (" New Book Added Succecfully. ")
       # messagebox.showinfo (  " Success ","New Book Added Succecfully !")
    


    def viewBook (self):
        if not self.books:
            #messagebox.showerror("Error", "No Books Available")
            print ("ERROR ! No Books avilable ")
            return
        
        for book in self.books :
            book.DisplayBookDetails() 
            print ("#" * 50)
    
    def searchBook(self):
        searchTerm = input("Enter Book ID or Book Title for search: ")
    
        for book in self.books:
           if book.id == searchTerm or book.title.lower() == searchTerm.lower():
              print(" Book Found!")
              book.DisplayBookDetails()
              #book.DisplayMessageBox() 
              return
    
        print(" Book Not Found!")
        #messagebox.showerror("Error", "Book Not Found!")

 
    

    def updateBook (self, Id, newTitle=None, newAuthor=None, newYear=None):
        for book in self.books:
            if book.id == Id:
                if newTitle:
                    book.title = newTitle
                if newAuthor:
                    book.author = newAuthor
                if newYear:
                    book.year = newYear
                print ("Book details updated successfully!")
                # messagebox.showinfo("Success", "Book details updated successfully!")
                return
        print("Book not found !")
        #messagebox.showerror("Error", "Book not found!")

    def deleteBook(self, Id):
        for book in self.books:
            if book.id == Id:
                self.books.remove(book)
                print ("Book Deleted Succesfully !")
                # messagebox.showinfo("Success", "Book deleted successfully!")
                return
        #messagebox.showerror("Error", "Book not found!")
        print ("Book Not Found !")