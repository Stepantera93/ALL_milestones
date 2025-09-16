# Клас Book представляє одну книгу
class Book:
    def __init__(self, title: str, category: str):
        self.title = title
        self.category = category

    def __repr__(self):
        return f"{self.title} ({self.category})"


# Клас Shelf зберігає список книг
class Shelf:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def sort_books(self):
        # сортуємо книги за алфавітом
        self.books.sort(key=lambda b: b.title)


# Клас Room — набір полиць
class Room:
    def __init__(self):
        self.shelves = []

    def add_shelf(self, shelf):
        self.shelves.append(shelf)

    def show(self):
        for i, shelf in enumerate(self.shelves, 1):
            if shelf.books:  # перевіряємо, що є книги
                category = shelf.books[0].category  # беремо категорію першої книги
                print(f"Shelf {i} ({category}): {shelf.books}")
            else:
                print(f"Shelf {i}: (empty)")


from faker import Faker
import random

# створюємо генератор Faker
fake = Faker()

# можливі категорії книг
categories = ["Fantasy", "Education", "Science", "History", "Biography"]

# генеруємо випадкові книги
books = [Book(fake.sentence(nb_words=3), random.choice(categories)) for _ in range(10)]


# автоматично створюємо полиці за категоріями
shelves = {}
for book in books:
    if book.category not in shelves:
        shelves[book.category] = Shelf()
    shelves[book.category].add_book(book)

# сортуємо книги на кожній полиці
for shelf in shelves.values():
    shelf.sort_books()

# додаємо полиці в кімнату
room = Room()
for shelf in shelves.values():
    room.add_shelf(shelf)

# виводимо результат
room.show()