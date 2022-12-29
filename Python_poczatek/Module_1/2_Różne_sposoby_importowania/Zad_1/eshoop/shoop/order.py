from .store import list_of_products, update_quantiny


orders = [
    {
        "products": "chleb",
        "quantiny": 10,
        "total price": 35
    }
]

def creative_new_order(products_name, quantiny):
    price = list_of_products[products_name]["price"]
    available_quantiny = list_of_products[products_name]["quantiny"]

    if available_quantiny < quantiny:
        print("Nie mamy tyle towaru")
        return None

    total_price = price * quantiny
    new_order = {
        "product": products_name,
        "quantiny": quantiny,
        "total_price": total_price
    }
    update_quantiny(products_name, quantiny)
    orders.append(dict(new_order))
    return new_order


