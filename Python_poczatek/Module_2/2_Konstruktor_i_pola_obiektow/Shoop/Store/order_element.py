from Store.product_and_other import Product
class OrderElement:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_order_elements_price(self):
        return self.product.price * self.quantity
    def print_positions(self):
        self.product.print_product()
        print(f" x {self.quantity}")


