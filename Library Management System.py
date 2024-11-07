class Book:

    def __init__(self):
        self.books = {}
        self.borrowed_books = []
        self.authors = {}

    def add_book(self, title, author_name, quantity):
        self.books[title] = {"author": author_name, "quantity": quantity, "available": True}
        print(f"---Book '{title}' added successfully!!---")

    def borrow_book(self, title):
        if title in self.books:
            if self.books[title]["available"]:
                self.books[title]["available"] = False
                print(f"---{title} has been borrowed!---")
            else:
                print(f"---Sorry, {title} is not available!!---")
        else:
            print(f"---Book '{title}' not found in the library!---")
        self.borrowed_books.append(title)

    def return_book(self, title):
        if title in self.books:
            if not self.books[title]["available"]:
                self.books[title]["available"] = True
                print(f"---Book '{title}' returned successfully.---")
            else:
                print(f"---Book '{title}' was not borrowed.---")
        else:
            print(f"---Book '{title}' not found in the library.---")

    def search_book(self, title):
        if title in self.books:
            print(f"Title: {title}")
            print(f"Author: {self.books[title]['author']}")
            print(f"Available: {self.books[title]['available']}")
        else:
            print("---Book not found in the library!---")

    def display_all_books(self):
        if self.books:
            print("Available Books:")
            for title, book_data in self.books.items():
                status = "Available" if book_data["available"] else "Borrowed"
                print(f"{title} by {book_data['author']}, {book_data['quantity']} copies. ({status})")
        else:
            print("---The library is empty.---")

class User:

    def __init__(self):
        self.__users = {}

    def set__add_user(self, user_id, name):
        if user_id not in self.__users:
            self.__users[user_id] = {'user_id': user_id, 'name': name}
            print("---User successfully added!---")
        else:
            print("User ID already in system.")

    def get__view_user(self, user_id):
        user = self.__users[user_id]
        if user_id in self.__users:
            print(f"User ID: {user['user_id']}")
            print(f"Name: {user['name']}")
        else:
            print("---User not found.---")

    def get__display_users(self):
        if not self.__users:
            print("---No users found.---")
        else:
            print("---List of users: ---")
        for user in self.__users.values():
            print(f"User ID: {user['user_id']}, Name: {user['name']}")

class Author:

    def __init__(self):
        self.authors = []
        self.author_books = []
        self.books = {}

    def add_author(self, author_name):
        if author_name not in self.authors:
            self.authors.append(author_name)
            print(f"---Author {author_name} successfully added!!---")
        else:
            print(f"---Author {author_name} already in system!!---")

    def view_author(self, author_books, author_name):
        # author_books = []
        for book in self.books:
            if self.authors == author_name:
                author_books.append(book)

        if self.author_books:
            print(f"---Books by {author_name}: ---")
            for book in author_books:
                print(f" - {book.title}")
        else:
            print(f"---No books found by {author_name}---")

    def display_authors(self):
        # self.authors = []
        if not self.authors:
            print("---No authors found.---")
        else:
            print("---Authors in the library: ---")
            for author in self.authors:
                print(f"Name: {author}")

class UserInterface:
    
    def __init__(self):
        self.book = Book()
        self.user = User()
        self.author = Author()

    def main(self):
        while True:
            print("Welcome to the Library Management System")
            print("---Book---")
            print("1. Add a New Book")
            print("2. Borrow a Book")
            print("3. Return a Book")
            print("4. Search for a Book")
            print("5. Display all Books")
            print("---User Menu---")
            print("6. Add a New User")
            print("7. View User Details")
            print("8. Display all Users")
            print("---Author Menu---")
            print("9. Add a New Author")
            print("10. View Author Details")
            print("11. Display all Authors")
            print("12. Quit")

            choice = input("Please choose an option (1-12): ")

            if choice == '1':
                title = input("Please enter the book title: ")
                author = input("Please enter the author name: ")
                quantity = input("Please enter quantity of book: ")
                self.book.add_book(title, author, quantity)
            elif choice == '2':
                title = input("Please enter the book title: ")
                self.book.borrow_book( title)
            elif choice == '3':
                title = input("Please enter the book title: ")
                self.book.return_book(title)
            elif choice == '4':
                title = input("Please enter the book title: ")
                self.book.search_book(title)
            elif choice == '5':
                self.book.display_all_books()

            elif choice == '6':
                name = input("Please enter user name: ")
                user_id = input("Please enter user ID: ")
                self.user.set__add_user(user_id, name)
            elif choice == '7':
                user_id = input("Please enter user id: ")
                self.user.get__view_user(user_id)
            elif choice == '8':
                self.user.get__display_users()

            elif choice == '9':
                author_name = input("Please enter the author's name: ")
                self.author.add_author(author_name)
            elif choice == '10':
                author = input("Please enter author's name: ")
                self.author.view_author(author, author_name)
            elif choice == '11':
                self.author.display_authors()
            elif choice == '12':
                print("Exiting the Library Management System!!")
                print("Thank you! Come Again!!!")
                break
            else:
                print("Invalid choice. Please try again")

if __name__ == "__main__":
    use_book = Book()
    user_info = User()
    use_author = Author()
    user_interface = UserInterface()
    user_interface.main()
