# Task 1
class Car:
    manufacturer = 'Toyota'
print(Car.manufacturer)
class Bike:
    manufacturer = 'Yamaha'
print(Bike.manufacturer)
# Task 2
class Book:
    publisher = "Penquin"

    def __init__(self, title, author ,year):
        self.title = title
        self.author = author
        self.year = year

book1 = Book('The Little Prince',  ' Antoine de Saint-Exupéry', '1943')
book2 = Book('Harry Potter',  ' J. K. Rowling', '1997')
print(Book.publisher)
print(f'{book1.title} is written by:  {book1.author}')
print(f'{book2.title} is written by:  {book2.author}')