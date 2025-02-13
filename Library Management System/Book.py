import tkinter as tk
from tkinter import messagebox

class Book :
    
    def __init__(self , id , title , author , publicationYear):
       
        self.id = id 
        self.title = title
        self.author = author
        self.publicationYear = publicationYear
    
    #Function To Display Book Details
    def DisplayBookDetails(self):
        print("\t\t Book Details ")
        print("ID:", self.id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publicationYear)
    
    # Display Message box with Book Details
    #def DisplayMessageBox(self):
         #Bookdetails = f"ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publicationYear}"
        # messagebox.showinfo("Book Details", Bookdetails)