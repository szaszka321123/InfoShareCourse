from Store.product_and_other import Product
from Store.order_element import OrderElement
import random
from Store.discount_policy import chrismas_discountu, constant_customer, normal_customer
class Order:

    MAX_ORDER_ELEMENT_LIMIT = 20
    def __init__(self, first_name, second_name, positions_list=None, discount_policy=None):
        self.second_name = second_name
        self.first_name = first_name
        if positions_list is None:
            positions_list = []
        if len(positions_list) > Order.MAX_ORDER_ELEMENT_LIMIT:
            self._positions_list = positions_list[:Order.MAX_ORDER_ELEMENT_LIMIT]
        else:
            self._positions_list = positions_list
        if discount_policy is None:
            discount_policy = normal_customer
        self.discount = discount_policy
        self.total_price = self._total_price_elements()


    @property
    def position_list(self):
        return self._positions_list


    def _total_price_elements(self):
        total_price = 0
        for elements in self._positions_list:
            total_price += elements.calculate_order_elements_price()
        if self.discount != normal_customer:
            if self.discount == "constant_customer":
                return constant_customer(total_price)
            else:
                return chrismas_discountu(total_price)
        else:
            return normal_customer(total_price)


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
