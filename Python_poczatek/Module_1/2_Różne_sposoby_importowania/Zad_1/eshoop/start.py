from shoop.order import creative_new_order

def run_online_shoop():
    print("Witaj w naszym sklepie!")
    name = input(f"Podaj nazwę produktu jaki chcesz dodać do koszyka: ")
    value = int(input(f"Podaj ilość produktu jaką chcesz zakupić: "))

    result = creative_new_order(products_name=name, quantiny=value)
    if result is not None:
        total_price = result["total_price"]
        print(f"Łączny koszt wyniesie : {total_price} Pln")


if __name__ == '__main__':
    run_online_shoop()



