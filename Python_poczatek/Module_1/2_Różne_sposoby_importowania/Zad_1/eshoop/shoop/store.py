
list_of_products = {
    "Chleb": {
        "prize": 3.5,
        "quantiny": 200
    },
    "Masło": {
        "prize": 5.99,
        "quantiny": 1200
    },
    "Jabłka": {
        "prize": 7.99,
        "quantiny KG": 80
    }
}

def update_quantiny(product_name, products_quantiny):
    list_of_products[product_name]["quantiny"] -= products_quantiny
