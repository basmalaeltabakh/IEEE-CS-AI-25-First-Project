import tkinter as tk
from tkinter import messagebox

class Book:
    def __init__(self, book_id, title, author, publication_year):
        self.id = book_id
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_details(self):
        print("\nBook Details ")
        print(f"ID: {self.id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")

    def display_message_box(self):
        book_details = f"ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}"
        messagebox.showinfo("Book Details", book_details)

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Year: {self.publication_year}"

    def dectionarize(self):
        return {"book_id": self.id, "title": self.title, "author": self.author, "publication_year": self.publication_year}
