def calculate_net_price(price, tax_rate=0.40):
    final_price = price + (price*tax_rate)
    return final_price

print(calculate_net_price(100))