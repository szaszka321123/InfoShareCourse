from Store.product_and_other import Product
from Store.order_element import OrderElement
import random
class Order:

    MAX_ORDER_ELEMENT_LIMIT = 20
    def __init__(self, first_name, second_name, positions_list=None):
        self.second_name = second_name
        self.first_name = first_name
        if positions_list is None:
            positions_list = []
        if len(positions_list) > Order.MAX_ORDER_ELEMENT_LIMIT:
            self._positions_list = positions_list[:Order.MAX_ORDER_ELEMENT_LIMIT]
        else:
            self._positions_list = positions_list
        self.total_price = self._total_price_elements()

    def _total_price_elements(self):
        total_price = 0
        for elements in self._positions_list:
            total_price += elements.calculate_order_elements_price()
        return total_price

    def add_new_product(self, product, quantity):
        if len(self._positions_list) >= Order.MAX_ORDER_ELEMENT_LIMIT:
            print(f"Brak możliwości dodania produktu, przekroczono limit w zamówieniu")
        else:
            self._positions_list.append(OrderElement(product, quantity))
            self.total_price = self._total_price_elements()

    def __str__(self):
        information_result = f"\n Imię: {self.first_name}| Nazwisko: {self.second_name} \n Wartość zamówienia {self.total_price}"
        product_result = "\t Zamówione produkty:\n"
        for element in self._positions_list:
            product_result += f"\t{element}\n"

        result = "\n".join([information_result, product_result])
        return result
    def __len__(self):
        return len(self._positions_list)
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if len(self._positions_list) != len(other._positions_list):
            return False
        if self.first_name != other.first_name or self.second_name != other.second.name:
            return False
        for position_list in self._positions_list:
            if position_list not in other.positions_list:
                return False
        return True


    @classmethod
    def generator_order(cls):
        number_order = random.randint(1, 40)
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


