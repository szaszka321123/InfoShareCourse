from Store.product_and_other import print_product, cookies
import random
class Order:

    def __init__(self, first_name, second_name, products=None):
        self.second_name = second_name
        self.first_name = first_name
        if products is None:
            products = []
        self.products = products

        total_price = 0
        for product in products:
            if product is int:
                total_price += product
        self.total_price = total_price

empty_order = Order(first_name="Daniel", second_name="Iwanowski")
eny_order = Order(first_name="Daniel", second_name="Iwanowski", products=[cookies])

def prind_order(Order):
    print("-" * 20)
    print(f"Imię: {Order.first_name}")
    print(f"Nazwisko: {Order.second_name}")
    print(f"Lista produktów {Order.products}")
    print(f"Wartość zamówienia {Order.total_price}zł")
    for product in Order.products:
        print("\t", end="")
        print_product(product)
    print("-" * 20)



first_order = Order(first_name="Daniel", second_name="Iwanowski", products=[cookies])

def generator_order():
    number_order = random.randint(1, 20)
    for eny_number in range(number_order):
        product_number = random.randint(1, 10)
        product_list = []
        for product in range(product_number):
            new_product = f"Produkt {product}"
            product_list.append(new_product)
        new_order = Order(first_name="Imię klijęta", second_name="Nazwisko klijęta", products=product_list)

    return new_order

