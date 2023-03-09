from Store.klasa_Apple import Apple
from Store.Klasa_Patato import Potato
from Store.order_and_other import Order, generator_order
from Store.product_and_other import Product
from Store.order_element import OrderElement


def run_example():

    first_order = generator_order()
    print(first_order)
    print(f"Liczba pozycji w zamówieniu: {len(first_order)}\n\n")
    second_order = generator_order()
    print(second_order)
    print(f"Liczba pozycji w zamówieniu: {len(second_order)}\n\n")

    nice_apple = Apple(kind="Green", size="Medium", price=3.78, weight=4)
    print(repr(nice_apple))
    print("\n\n")
    old_potato = Potato(kind="Old", size="H", price=3.69, weight_potato=10)
    print(repr(old_potato))

    other_salat = Product(name="Green salat", cathegory="Vegetable", price=8.99)
    new_other_order = Product(name="Green salat", cathegory="Vegetable", price=8.99)
    first_element = OrderElement(product="Marchewki", quantity=20)
    second_element = OrderElement(product="Marchewki", quantity=20)
    print("\n\n")

    print(first_element == second_element)
    print(first_order == second_order)
    print(other_salat == new_other_order)

    print("\n\n")

    third_order = generator_order()
    print(third_order)
    new_product = Product(name="Maka", cathegory="Food", price=10.99)
    third_order.add_new_product(product=new_product, quantity=6)
    print(third_order)


if __name__ == "__main__":

    run_example()
