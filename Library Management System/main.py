from Library import Library

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Save to File")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        match choice:
            case "1":
                library.add_book()
            case "2":
                library.view_books()
            case "3" :
                library.search_book()
            case "4" :
                library.save_to_file()
            case "5":
                print("Exiting the system. Goodbye!")
                break
            case _:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
