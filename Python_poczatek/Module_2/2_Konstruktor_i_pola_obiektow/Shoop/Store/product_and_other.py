class Product:

    def __init__(self, name, cathegory, price):
        self.price = price
        self.cathegory = cathegory
        self.name = name

eny_product = Product(name="Butter", cathegory="food", price=5.29)

def print_product(message):
    print(f"Twój produkt to: {cookies.name} - Katergoria: {cookies.cathegory} - Cena jednostkowa: {cookies.price}")

cookies = Product(name="Cookies", cathegory="Sweets", price=7.99)

