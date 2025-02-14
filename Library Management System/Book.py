
class Book:
    def __init__(self,Id,ISBN,  title, author, publicationYear):
        self.Id = Id
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.publicationYear = publicationYear
    
    # Display Book Details 
    def DisplayBookDetails(self):
        print("\t\t Book Details ")
        print("ID:", self.Id)
        print("ISBN:", self.ISBN)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publicationYear)

    # Function to convert book data into a dictionary (for JSON storage)
    def dictionarize(self):
        return {
            "Id": self.Id,
            "ISBN":self.ISBN,
            "title": self.title,
            "author": self.author,
            "publicationYear": self.publicationYear
        }