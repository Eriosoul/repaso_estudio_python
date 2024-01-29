class Book:
    def __init__(self, title, author, ):
        self.title = title
        self.author = author

    def __str__(self):
        return f'Book: [Title: {self.title}, author: {self.author}]'
