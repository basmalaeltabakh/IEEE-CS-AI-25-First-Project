
class Book:
    def __init__(self, Id, title, author, publicationYear):
        self.Id = Id
        self.title = title
        self.author = author
        self.publicationYear = publicationYear
    
    # Display Book Details 
    def DisplayBookDetails(self):
        print("\t\t Book Details ")
        print("ID:", self.Id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publicationYear)

    # Function to convert book data into a dictionary (for JSON storage)
    def dictionarize(self):
        return {
            "Id": self.Id,
            "title": self.title,
            "author": self.author,
            "publicationYear": self.publicationYear
        }