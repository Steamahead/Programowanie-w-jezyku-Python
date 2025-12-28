class Order:
    def __init__(self, employee, student, books, order_date):
        self.order_date = order_date
        self.employee = employee
        self.student = student
        self.books = books

    def __str__(self):
        return f'Data zamówienia {self.order_date}, Książki: {self.books}'
