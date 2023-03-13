from Store.klasa_Apple import Apple
from Store.Klasa_Patato import Potato
from Store.order_and_other import Order
from Store.product_and_other import Product
from Store.order_element import OrderElement
from Store.klasa_TaxCalculator import TaxCalculator

def run_example():

    # first_order = Order.generator_order()
    # print(first_order)
    # print(f"Liczba pozycji w zamówieniu: {len(first_order)}\n\n")
    # second_order = Order.generator_order()
    # print(second_order)
    # print(f"Liczba pozycji w zamówieniu: {len(second_order)}\n\n")
    #
    # nice_apple = Apple(kind="Green", size="Medium", price=3.78, weight=4)
    # print(repr(nice_apple))
    # print("\n\n")
    # old_potato = Potato(kind="Old", size="H", price=3.69, weight_potato=10)
    # print(repr(old_potato))
    #
    # # other_salat = Product(name="Green salat", cathegory="Vegetable", price=8.99)
    # # new_other_order = Product(name="Green salat", cathegory="Vegetable", price=8.99)
    # # first_element = OrderElement(product="Marchewki", quantity=20)
    # # second_element = OrderElement(product="Marchewki", quantity=20)
    # # print("\n\n")
    # #
    # # # print(first_element == second_element)
    # # # print(first_order == second_order)
    # # # print(other_salat == new_other_order)
    #
    # print("\n\n")
    #
    # third_order = Order.generator_order()
    # print(third_order)
    # new_product = Product(name="Maka", cathegory="Food", price=10.99)
    # third_order.add_new_product(product=new_product, quantity=6)
    # print(third_order)

    chicken_product = Product(name="chicken", cathegory="Food", price=21.99)
    tax_result = TaxCalculator.calculation_value_taxes(chicken_product)
    print(tax_result)
    other_product = Product(name="Orange", cathegory="Fruit", price=12.99)
    next_tax_result = TaxCalculator.calculation_value_taxes(other_product)
    print(next_tax_result)


if __name__ == "__main__":

    run_example()
