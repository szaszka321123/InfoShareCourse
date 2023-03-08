from Store.product_and_other import Product
import random
class Order:

    def __init__(self, first_name, second_name, products=None):
        self.second_name = second_name
        self.first_name = first_name
        if products is None:
            products = []
        self.products = products

    def total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.price
        self.total_price = total_price


    def prind_order(self):
        print("-" * 20)
        print(f"Imię: {self.first_name}")
        print(f"Nazwisko: {self.second_name}")
        print(f"Lista Zamowien {self.products}")
        print(f"Wartość zamówienia {self.total_price}zł")
        for product in self.products:
            print("\t", end="")
            product.print_product()
        print("-" * 20)



def generator_order():
    number_order = random.randint(1, 20)
    product_list = []
    for eny_number in range(number_order):
        new_product = f"Produkt {eny_number}"
        cathegory = "Inne"
        product_number = random.randint(1, 10)
        new_order = Product(new_product, cathegory, price={product_number})
        product_list.append(new_order)
    new_1 = Order(first_name="Imię klijęta", second_name="Nazwisko klijęta", products=product_list)

    return new_1


