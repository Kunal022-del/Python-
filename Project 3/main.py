class Library:
    def __init__(self, listOfBooks):
        self.Books = listOfBooks

    def displayAvailableBooks(self):
        print("\n" "Books present in this library are:\n")
        for i in range(len(self.Books)):
            print(f"{i + 1}. {self.Books[i]}")

    def borrowBook(self, BookName):
        if BookName in self.Books:
            print(
                f"You have been issued {BookName}. Please keep it safe and return it within 15 days"
            )
            self.Books.remove(BookName)
            return True
        else:
            print(
                "Sorry, This Book is either not available or has already been issued to someone else. Please wait until the Book is available"
            )
            return False

    def returnBook(self, BookName):
        self.Books.append(BookName)
        print("Thanks for returning this Book! Hope you enjoyed reading it.")


class Student:
    def requestBook(self):
        self.Book = input("Enter the name of the Book you want to borrow: ")
        return self.Book

    def returnBook(self):
        self.Book = input("Enter the name of the Book you want to return: ")
        return self.Book


centraLibrary = Library(
    ["Algorithms", "Django", "Clrs", "Node js", "PHP", "Python", "C++ Sharp"]
)
student = Student()
while True:
    welcome_message = """\n----- Welcome to Central Library -----
        Please choose an option:
        1. List all the Books
        2. Request a Book
        3. Add/Return a Book
        4. Exit the Library
        """
    print(welcome_message)
    a = int(input("Enter a choice: "))
    if a == 1:
        centraLibrary.displayAvailableBooks()
    elif a == 2:
        centraLibrary.borrowBook(student.requestBook())
    elif a == 3:
        centraLibrary.returnBook(student.returnBook())
    elif a == 4:
        print("Thanks for choosing Central Library. Have a great day ahead!")
        exit()
    else:
        print("Invalid Choice!")
