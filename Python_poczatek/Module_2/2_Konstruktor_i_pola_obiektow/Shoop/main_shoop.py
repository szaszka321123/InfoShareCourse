from Store.klasa_Apple import Apple
from Store.Klasa_Patato import Potato
from Store.order_and_other import Order, generator_order
from Store.product_and_other import Product

def run_example():

    first_order = generator_order()
    print(first_order)
    print(f"Liczba pozycji w zamówieniu: {len(first_order)}\n\n")
    second_order = generator_order()
    print(second_order)
    print(f"Liczba pozycji w zamówieniu: {len(second_order)}\n\n")

    green_apple = Apple(kind="Green", size="Medium", price=3.78, weight=4)
    print(repr(green_apple))
    print("\n\n")
    old_potato = Potato(kind="Old", size="H", price=3.69, weight_potato=10)
    print(repr(old_potato))

if __name__ == "__main__":

    run_example()