books = []

def add_book(title, author, isbn):
    book = {
        'title': title,
        'author': author,
        'isbn': isbn,
        'available': True
    }
    books.append(book)
    print(f"book{title} added successfuly!")
    return book

def find_book(isbn):
    for book in books:
        if book['isbn']== isbn:
            return book
        return None
    