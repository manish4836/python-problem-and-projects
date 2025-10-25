prices = [100, 250, 45, 999, 1500, 75, 3000]

def add_tax(price, tax=0.10):
    return price + (price * tax)

new_list = list(map(lambda x: add_tax(x), prices))
print(new_list)