from product_and_other import Product
    class OrderElement():
        def __init__(self, product, quantity):
            self.quantity = quantity
            self.product = product

        def calculate_order_elements_price(self):
            total_price = self.product.price() * self.quantity()
            print(f"Całkowita cena pozycji wynosi:{total_price} Zł")
        def print_positions(self):
            self.product.print_product()
            print(f" x {self.quantity}")

