class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library located at: {self.city}, 'Street name:' {self.street}, 'Zip code:' {self.zip_code}, 'Open hours:' {self.open_hours}, 'Phone number:' {self.phone}"
 class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}, 'Hire date:' {self.hire_date}, 'Birth date:' {self.birth_date}, 'City:' {self.city}, 'Street:' {self.street}, 'Zip code:' {self.zip_code}, 'Phone number:' {self.phone}"