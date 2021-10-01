class Library:
    def __init__(self, List_Of_Books, Library_Name):
        self.List_Of_Books = List_Of_Books
        self.Library_Name = Library_Name
        self.Lend_Data = {}
        for book in self.List_Of_Books:
            self.Lend_Data[book] = None

    def display_books(self):
        print(f"Our {self.Library_Name} has the following books: ")
        for book in self.List_Of_Books:
            print(book)

    def lend_book(self, Book_Name, Reader_Name):
        if Book_Name in self.List_Of_Books:
            if self.Lend_Data[Book_Name] is None:
                self.Lend_Data[Book_Name] = Reader_Name
                print(f"{Book_Name} Succesfully Lent.")
            elif self.Lend_Data[Book_Name] is not None:
                print(
                    f"Sorry! This Book Is Already Lent To {self.Lend_Data[Book_Name]}.")
        else:
            print(
                f"Sorry! The Entered Is Not Available Or You Have Entered Wrong Book Name.")

    def return_book(self, Book_Name, Reader_Name):
        if self.Lend_Data[Book_Name] is not None:
            self.Lend_Data.pop(Book_Name)
            self.List_Of_Books.append(Book_Name)
            print(f"{Book_Name} Was Succesfully Returned.")
        elif self.Lend_Data[Book_Name] is None:
            print(f"Sorry! {Book_Name} Is Not Lent")

    def add_book(self, Book):
        self.List_Of_Books.append(Book)
        self.Lend_Data[Book] = None
        print(f"{Book} Successfully Added.")

    def remove_book(self, Book):
        self.List_Of_Books.remove(Book)
        self.Lend_Data.pop(Book)
        print(f"{Book} Succesfully Removed")

    def Lend_Database(self, Pass):
        if Pass == 112233:
            print(self.Lend_Data)
        elif Pass != 112233:
            print("The entered password is wrong.")


list_books = ["Harry Potter", "Python Notes",
              "Java Notes", "C++ Notes", "CSS Notes"]
library_name = "Central Library"
central_library = Library(list_books, library_name)
secret_key = 123


def app():

    print(f"""-----Welcome To {library_name}-----
Press:
0 To Quit
1 To Display Books
2 To Lend Book
3 To Return Book
4 To Add Book
5 To Remove Book
6 To See Database
""")

    Exit = True
    while Exit == True:
        _input = input("Enter: ")

        if _input == "1":
            central_library.display_books()

        elif _input == "2":
            inp = input("Enter Book Name: ")
            inp2 = input("Enter Reader Name: ")
            central_library.lend_book(inp, inp2)

        elif _input == "3":
            inp = input("Enter Book Name: ")
            inp2 = input("Enter Reader Name: ")
            central_library.return_book(inp, inp2)

        elif _input == "4":
            inp = input("Enter Book Name: ")
            central_library.add_book(inp)

        elif _input == "5":
            inp = input("Enter Book Name: ")
            central_library.remove_book(inp)

        elif _input == "6":
            inp = int(input("Enter Password: "))
            central_library.Lend_Database(inp)

        elif _input == "0":
            Exit = False

        elif _input != "0" and "1" and "2" and "3" and "4" and "5":
            print("Sorry! I Did'nt Understand")


key = int(input("Enter Security Key Of Library:\n"))
if key == secret_key:
    if __name__ == "__main__":
        app()
elif key != secret_key:
    print(f"The Key You Entered Is Wrong.")
