class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        current_year = 2026
        return current_year - self.publication_year

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


# Example usage
book1 = Book("Python Basics", "John Smith", "123456789", 2020)

print(book1.get_summary())
print("Book Age:", book1.get_age(), "years")