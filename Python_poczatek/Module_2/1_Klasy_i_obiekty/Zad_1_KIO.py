class Products:
    pass

class Order:
    pass

class Apple:
    pass

class Potato:
    pass

jablko = Apple()
ziemniak = Potato()

print(type(jablko))
print(type(ziemniak))
products_dict = {
    "butter": Products(),
    "soap": Products(),
    "papier": Products()
}
products_list = [Order(), Order(), Order(), Order(), Order()]
print(products_list)
print(products_dict)