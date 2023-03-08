class Product:

    def __init__(self, name, cathegory, price):
        self.name = name
        self.cathegory = cathegory
        self.price = price



    def print_product(self):
        print(f"Twój produkt to: {self.name} - Katergoria: {self.cathegory} - Cena jednostkowa: {self.price}/szt")



