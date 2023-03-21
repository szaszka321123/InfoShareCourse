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

class ExpiringProduct(Product):

    def __init__(self, name, cathegory, price, year_of_production, years_validity):
        super().__init__(name, cathegory, price)
        self.years_validity = years_validity
        self.year_of_production = year_of_production

    def does_expire(self, current_year):
        if current_year > (self.year_of_production + self.years_validity):
            print(f"Data ważności upłyneła w {self.year_of_production + self.years_validity}")
        else:
            print(f"Produkt nadaje się jeszcze do sporzycia")




