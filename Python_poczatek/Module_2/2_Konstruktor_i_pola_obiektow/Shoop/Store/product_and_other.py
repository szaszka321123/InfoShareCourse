class Product:

    def __init__(self, name, cathegory, price):
        self.price = price
        self.cathegory = cathegory
        self.name = name



    def print_product(self):
        print(f"Twój produkt to: {self.name} - Katergoria: {self.cathegory} - Cena jednostkowa: {self.price}")



