shopping_cart = [
    {'item': 'Laptop', 'price': 1200, 'quantity': 1},
    {'item': 'Mouse', 'price': 25, 'quantity': 3},
    {'item': 'Keyboard', 'price': 75, 'quantity': 2},
]
def sort_list(values):
    return sorted(values,key= lambda values: values["price"] *values["quantity"])

sorted_list = sort_list(shopping_cart)
print(sorted_list)