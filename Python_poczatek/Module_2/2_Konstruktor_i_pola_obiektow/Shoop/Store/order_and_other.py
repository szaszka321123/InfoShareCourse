from Store.product_and_other import Product
from Store.order_element import OrderElement
import random
from Store.discount_policy import DiscountPolicy, AbsoluteDiscount, PercentageDiscount
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
            discount_policy = DiscountPolicy()
        self.discount = discount_policy

    @property
    def total_price(self):
        total_price = 0
        for elements in self._positions_list:
            total_price += elements.calculate_order_elements_price()
        return self.discount.apply_discount(total_price)


    def add_new_product(self, product, quantity):
        if len(self._positions_list) >= Order.MAX_ORDER_ELEMENT_LIMIT:
            print(f"Brak możliwości dodania produktu, przekroczono limit w zamówieniu")
        else:
            self._positions_list.append(OrderElement(product, quantity))

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
        if len(self._positions_list) != len(other.positions_list):
            return False
        if self.first_name != other.first_name or self.second_name != other.second.name:
            return False
        for position_list in self._positions_list:
            if position_list not in other.positions_list:
                return False
        return True

    @property
    def position_list(self):
        return self._positions_list

    @position_list.setter
    def position_list(self, value):
        if len(value) <= Order.MAX_ORDER_ELEMENT_LIMIT:
            self._positions_list = value
        else:
            self._positions_list = value[:Order.MAX_ORDER_ELEMENT_LIMIT]

class ExpressOrder(Order):

    EXPRESS_DELIVERY_FEE = 4.99

    def __init__(self, first_name, second_name, position_list, discount_policy, delivery):
        super(ExpressOrder, self).__init__(first_name, second_name, position_list, discount_policy)
        self.delivery = delivery

    @property
    def delivery_fee(self):
        return super().total_price + ExpressOrder.EXPRESS_DELIVERY_FEE

    def __str__(self):
        information_result = f"Expresowe zamówienie złożone przez:" \
                             f"\n Imię: {self.first_name} | Nazwisko: {self.second_name} \n Wartość zamówienia {self.total_price} zł \n" \
                             f" Termin dostawy: {self.delivery} \n Koszt dostawy doliczony do wartości zamówienia {self.delivery_fee} zł"
        product_result = "\t Zamówione produkty:\n"
        for element in self._positions_list:
            product_result += f"\t{element}\n"

        result = "\n".join([information_result, product_result])
        return result
