class Book:
    def __init__(self, title, author, price, is_available = True):
        self.title = title
        self.author = author
        self.price = price
        self.is_available = is_available

    def display_book_info(self):
        print(f"Book Name: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        print(f"Available: {'yes' if self.is_available else 'no'}")

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"You have successfully borrowed {self.title}.")
            return True
        else:
            print(f"Sorry, {self.title} is currently not available.")
            return False

    def return_book(self):
        self.is_available = True
        print(f"Thank you for returning {self.title}.")
        return True

book1 = Book("python programming", "john doe", 500.90)
book2 = Book("Data Structures", "Jane Smith", 600, False)

book1.display_book_info()
book2.display_book_info()


book1.borrow_book()
book1.borrow_book()
book2.borrow_book()

book1.display_book_info()


book1.return_book()
book1.return_book()
book2.return_book()

book1.display_book_info()