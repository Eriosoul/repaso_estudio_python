from book import Book


class LibrarySystem(Book):
    def __init__(self, title, author, available=0):
        super().__init__(title, author)
        self.available = available

    def __str__(self):
        return f'Available: {self.available} {super().__str__()}'
