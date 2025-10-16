

def create_counter():
    counter = 0
    def inner_counter():
        nonlocal counter
        counter += 1
        return counter
    return inner_counter

counter1 = create_counter()
print(counter1()) 
print(counter1())
print(counter1())
print(counter1())
