class Library:
    def __init__(self, listOfBooks):
        self.listOfBooks = listOfBooks

## displaying all the available books to user
    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.listOfBooks:
            print("\t * " + book)

## program for borrowing a book
    def borrowBook(self, bookName):
        if bookName in self.listOfBooks:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days.")
            self.listOfBooks.remove(bookName)
            return True
        else:
            print("Sorry, This book has already been issued to someone else. Please wait untill the book is returned.")
            return False

## returning/adding a book into library 
    def returnBook(self, bookName):
        self.listOfBooks.append(bookName)
        print("Thanks for returning/adding this book! Hope you enjoyed reading it. Have a great day ahead!")

## requesting and returning or adding a book by user 
class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow:\n")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return:\n")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "Clean Code", "Coding Journey Of Mr-Basit"])

student = Student()

## printing the manual of library
while(True):
    welcomeMsg = '''\n ====== Welcome to Central Library ======
    Please choose an option:
    1. List all the books
    2. Request a book
    3. Add/Return a book
    4. Exit the Library
    '''
    print(welcomeMsg)
    a = int(input("Enter a choice:"))
    if a == 1:
        centralLibrary.displayAvailableBooks()
    elif a == 2:
        centralLibrary.borrowBook(student.requestBook())
    elif a == 3:
        centralLibrary.returnBook(student.returnBook())
    elif a == 4:
        print("Thanks for choosing Central Library. Have a great day ahead!")
        exit()
    else:
        print("Invalid Choice!")
