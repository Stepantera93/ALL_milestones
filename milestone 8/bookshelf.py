"""
========================================
 UML Diagram for Milestone 8 — Bookshelf
========================================

+------------------+       # Клас Book — окрема книга
|      Book        |
+------------------+
| id: int          |       # Унікальний ідентифікатор книги
| title: str       |       # Назва книги
| category: str    |       # Категорія книги
+------------------+
| __repr__()       |       # Метод для відображення книги
+------------------+

+------------------+       # Клас Shelf — полиця для книг
|      Shelf       |
+------------------+
| books: list      |       # Список об’єктів Book, що зберігаються на полиці
+------------------+
| add_book(book)   |       # Додати книгу на полицю
| sort_books()     |       # Відсортувати книги за назвою
+------------------+

+------------------+       # Клас Room — кімната з полицями
|      Room        |
+------------------+
| id: int          |       # Унікальний ідентифікатор кімнати
| shelves: list    |       # Список полиць у кімнаті
+------------------+
| add_shelf(shelf) |       # Додати полицю в кімнату
| show()           |       # Відобразити вміст кімнати
+------------------+

Відносини:
- Room *--- Shelf  (кімната містить багато полиць)
- Shelf *--- Book  (полиця містить багато книг)
"""


# Клас Book представляє одну книгу
class Book:
    _id_counter = 1  # Лічильник для унікальних id

    def __init__(self, title: str, category: str):
        self.id = Book._id_counter
        Book._id_counter += 1
        self.title = title
        self.category = category

    def __repr__(self):
        return f"{self.id}: {self.title} ({self.category})"


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
    _id_counter = 1  # Лічильник для унікальних id

    def __init__(self):
        self.id = Room._id_counter
        Room._id_counter += 1
        self.shelves = []

    def add_shelf(self, shelf):
        self.shelves.append(shelf)

    def show(self):
        print(f"Room {self.id}:")
        for i, shelf in enumerate(self.shelves, 1):
            if shelf.books:  # перевіряємо, що є книги
                category = shelf.books[0].category  # беремо категорію першої книги
                print(f"  Shelf {i} ({category}): {shelf.books}")
            else:
                print(f"  Shelf {i}: (empty)")


from faker import Faker
import random

def generate_books(n=10):
    fake = Faker()
    categories = ["Fantasy", "Education", "Science", "History", "Biography"]
    return [Book(fake.sentence(nb_words=3), random.choice(categories)) for _ in range(n)]

# генеруємо випадкові книги
books = generate_books(10)

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