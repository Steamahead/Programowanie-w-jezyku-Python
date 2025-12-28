class Property:
    def __init__(self, area, rooms, price, adress):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.adress = adress

    def __str__(self):
        return f'Adres: {self.adress}, L.pokoi: {self.rooms}, Powierzchnia: {self.area}, Cena: {self.price}'

class House(Property):
    def __init__(self, area, rooms, price, adress, plot:int):
        super().__init__(area, rooms, price, adress)

        self.plot = plot

    def __str__(self):
        return super().__str__() + f', Rozmiar działki: {self.plot}'

h_object = House(120, 5, 900, "Gdańsk, ul. Słoneczna 15", 800)

class Flat(Property):
    def __init__(self, area, rooms:int, adress, floor, price):
        super().__init__(area, rooms, price, adress)

        self.floor = floor

    def __str__(self):
        return super().__str__() + f', Piętro: {self.floor} '

f_object = Flat(80, 3, "Poznań, ul. Krótka 8", 2, 400)

print(h_object)
print(f_object)