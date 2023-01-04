class Products:
    pass

class Order:
    pass

class Apple:
    pass

class Potato:
    pass

green_apple = Apple()
red_apple = Apple()
young_potato = Potato()
old_potato = Potato()

print(type(green_apple))
print(type(red_apple))
print(type(young_potato))
print(type(old_potato))

products_dict = {
    "butter": Products(),
    "soap": Products(),
    "papier": Products()
}
products_list = [Order(), Order(), Order(), Order(), Order()]
print(products_list)
print(products_dict)