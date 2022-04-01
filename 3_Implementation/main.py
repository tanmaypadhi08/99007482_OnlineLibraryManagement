# This online library management is made by Tanmay Padhi
class Library:
    #this library constructor has all the parameters needed to run the program
    def __init__(self, list, name,sug, delt,pswd,userid):
        # input the booklist in the given list
        self.bookslist = list
        # enter the name
        self.name = name
        # check whether the book is available or not
        self.lenddict = {}
        # suggestion of new books
        self.suggest = sug
        # delete the directory for empty books
        self.delete = delt
        # password for login
        self.password=pswd
        # username for login
        self.username= userid

    # function to display the available books
    def displaybooks(self):
        print(f"We have following books in our library {self.name}")
        for book in self.bookslist:
            print(book)

    # function to suggest new books to be added in the library
    def suggestbook(self, book1):
        print(f"Oops, looks like it was missing from the library {self.suggest}")
        self.suggest = book1
        if book1 in self.bookslist:
            print("Already There")
            print("Thank You for your suggestion")
        else:
            print("Thank You for your suggestion, We will add that book soon")

    # delete the directory for book with 0 entries in the database
    def deletebook(self, book2):
        print(f"So sorry to delete this from the library {self.deletebook}")
        self.delete = book2
        if book2 in self.bookslist:
            print("Okay, the book has been removed successfully")
        else:
            print("It was never included in our library")

    def lendbook(self, user, book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lenddict[book]}")

    def addbook(self, book):
        self.bookslist.append(book)
        print("Book has been added to the book list")

    def returnbook(self, book):
        self.lenddict.pop(book)
if __name__ == '__main__':
    tanmay = Library(['The Man who knew Infinity', 'Steve Jobs', 'Harry Potter', 'IKIGAI', 'The Monk Who Sold His Ferrari', 'Tanmay Padhi'], 'Tanmay Padhi', 'Tanmay Padhi', 'Delete Book','pswd','userid')

    userid=  input("Enter a username: ")
    pswd=  input("Enter a password: ")

    while True:
        print("**************Welcome****************")
        print(f"Welcome to the {tanmay.name} library")
        print("*************************************")

        print(f" What You Want To Have")

        print("1. Show available books")

        print("2. Issue Book")

        print("3. Add a new book")

        print("4. Return a Book")

        print("5. Suggest a Book")

        print("6. Delete a Book")

        print("7. Exit")

        print("**************************Enter your choice************************")

        user_choice = input()
        if user_choice not in ['1','2','3','4','5','6','7']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            id=input("Enter your user ID: ")
            passwd=input("Enter your password: ")
            while True:
                if userid==id:
                    tanmay.displaybooks()
                    break

                print("Incorrect")
                id = input("Enter your user ID: ")
                passwd = input("Enter your password: ")
                continue



        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            id = input("Enter your user ID: ")
            passwd = input("Enter your password: ")
            while True:
                if userid == id:
                    tanmay.lendbook(userid, book)
                    break

                print("Incorrect")
                id = input("Enter your user ID: ")
                passwd = input("Enter your password: ")
                continue


        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            id = input("Enter your user ID: ")
            passwd = input("Enter your password: ")
            while True:
                if userid == id:
                    tanmay.addbook(book)
                    break

                print("Incorrect")
                id = input("Enter your user ID: ")
                passwd = input("Enter your password: ")
                continue


        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            id = input("Enter your user ID: ")
            passwd = input("Enter your password: ")
            while True:
                if userid == id:
                        tanmay.returnbook(book)
                        break

                print("Incorrect")
                id = input("Enter your user ID: ")
                passwd = input("Enter your password: ")
                continue


        elif user_choice == 5:
            book1 = input("Enter the name of the book you want to suggest:")
            id = input("Enter your user ID: ")
            passwd = input("Enter your password: ")
            while True:
                if userid == id:
                    tanmay.suggestbook(book1)
                    break

            print("Incorrect")
            id = input("Enter your user ID: ")
            passwd = input("Enter your password: ")
            continue


        elif user_choice == 6:
            book2 = input("Name the book you want to remove:")
            id = input("Enter your user ID: ")
            passwd = input("Enter your password: ")
            while True:
                if userid == id:
                    tanmay.deletebook(book2)
                    break
            print("Incorrect")
            id = input("Enter your user ID: ")
            passwd = input("Enter your password: ")
            continue


        elif user_choice == 7:
            exit()

        else:
            print("Not a valid option")


        print("Press Q to Quit and C to Continue")
        user_choice2 = ""
        while(user_choice2!="c" or user_choice2!="q" or user_choice2!="Q" or user_choice2!="C"):

            user_choice2 = input()
            if user_choice2 == "q" or user_choice2 == "Q":
                print("Bubye")
                exit()

            elif user_choice2 == "c" or user_choice == "C":
                continue

