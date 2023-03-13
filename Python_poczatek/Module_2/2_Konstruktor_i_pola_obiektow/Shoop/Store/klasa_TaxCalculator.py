from Store.product_and_other import Product
class TaxCalculator:

    TAX_FRUIT_VEGETABLE = 0.05
    TAX_FOOD = 0.08
    TAX_OTHERS_PRODUCTS = 0.2

    @staticmethod
    def calculation_value_taxes(order_element):
        cathegory = order_element.cathegory
        if cathegory == "Fruit" or "Vegetables":
            tax_value = order_element.price * TaxCalculator.TAX_FRUIT_VEGETABLE
            return tax_value
        elif cathegory == "Food":
            tax_value = order_element.price * TaxCalculator.TAX_FOOD
            return tax_value
        else:
            tax_value = order_element.price * TaxCalculator.TAX_OTHERS_PRODUCTS
            return tax_value

