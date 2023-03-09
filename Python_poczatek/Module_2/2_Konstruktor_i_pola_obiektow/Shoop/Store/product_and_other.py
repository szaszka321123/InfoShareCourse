class Product:

    def __init__(self, name, cathegory, price):
        self.name = name
        self.cathegory = cathegory
        self.price = price



    def __str__(self):
        return f"Twój produkt to: {self.name} - Katergoria: {self.cathegory} - Cena jednostkowa: {self.price}/szt"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (self.name == other.name and
                self.cathegory == other.cathegory and
                self.price == other.price)
