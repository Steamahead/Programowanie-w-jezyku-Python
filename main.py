from library_app.library_class import Library
from library_app.book_class import Book
from library_app.employee_class import Employee
from library_app.order_class import Order

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
