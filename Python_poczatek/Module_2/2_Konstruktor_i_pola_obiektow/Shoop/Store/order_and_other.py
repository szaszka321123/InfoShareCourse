from Store.product_and_other import Product
from Store.order_element import OrderElement
import random
class Order:

    def __init__(self, first_name, second_name, positions_list=None):
        self.second_name = second_name
        self.first_name = first_name
        if positions_list is None:
            positions_list = []
        self.positions_list = positions_list
        self.total_price = self.total_price_elements()

    def total_price_elements(self):
        total_price = 0
        for elements in self.positions_list:
            total_price += elements.calculate_order_elements_price()
        return total_price



    def __str__(self):
        information_result = f"\n Imię: {self.first_name}| Nazwisko: {self.second_name} \n Wartość zamówienia {self.total_price}"
        product_result = "\t Zamówione produkty:\n"
        for element in self.positions_list:
            product_result += f"\t{element}\n"

        result = "\n".join([information_result, product_result])
        return result







def generator_order():
    number_order = random.randint(1, 20)
    position_list = []
    for eny_number in range(number_order):
        name_product = f"Produkt {eny_number}"
        cathegory = "Inne"
        product_number = random.randint(1, 10)
        new_product = Product(name=name_product, cathegory=cathegory, price=product_number)
        quantity_number = random.randint(1, 5)
        position_list.append(OrderElement(product=new_product, quantity=quantity_number))

    new_order = Order(first_name="Daniel", second_name="Iwanowski", positions_list=position_list)

    return new_order


