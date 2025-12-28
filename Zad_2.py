class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka: {self.city} ul. {self.street}'


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date,
                 city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Imię: {self.first_name}, Nazwisko: {self.last_name}'


class Book:
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f'Autor: {self.author_name} {self.author_surname}, '
                f'Własność: {self.library}')

    def __repr__(self):
        return str(self)


class Order:
    def __init__(self, employee, student, books, order_date):
        self.order_date = order_date
        self.employee = employee
        self.student = student
        self.books = books

    def __str__(self):
        return f'Data zamówienia {self.order_date}, Książki: {self.books}'


# Libraries
lib_waw = Library("Warszawa", "Marszałkowska 5", "00-100", "8-16", "123-456")
lib_rdm = Library("Radom", "Mickiewicza 6", "00-400", "8-16", "456-987")

# Books
b1 = Book(lib_waw, "1836", "Adam", "Mickiewicz", 300)
b2 = Book(lib_waw, "1890", "Bolesław", "Prus", 600)
b3 = Book(lib_rdm, "1950", "Stanisław", "Lem", 200)
b4 = Book(lib_rdm, "2020", "Olga", "Tokarczuk", 400)
b5 = Book(lib_waw, "1920", "Stefan", "Żeromski", 250)

# Employees
e1 = Employee("Adam", "Nowak", '2020',
              '1990', "Warszawa", "Miła", "03-193", '111002003')
e2 = Employee("Anna", "Nowak", "2021",
              "1992", "Kraków", "Y", "3030", "666666666")
e3 = Employee("Tomasz", "Zając", "2022",
              "1995", "Gdańsk", "Z", "8080", "777777777")

# Student
s1 = ("Kazik", "Staszewski")
s2 = ("Witold", "Senyszyn")
s3 = ('Jan', 'Wiatrak')

# Orders
o1 = Order(e1, s2, [b5, b4], '14.03.2024')
o2 = Order(e2, s1, [b3], '12.06.2025')


print(o1)
print(o2)
