
class LibrarySystem:
    def __init__(self, available=0):
        self.available = available

    def __str__(self):
        return f'Available: {self.available} {super().__str__()}'
