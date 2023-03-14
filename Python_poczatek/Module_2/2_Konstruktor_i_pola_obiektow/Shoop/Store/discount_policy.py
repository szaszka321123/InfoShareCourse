def normal_customer(order):
    return order

def constant_customer(order):
    return order * 0.95

def chrismas_discountu(order):
    if order > 100:
        return order - 20
    return order