def multiply_by(n):
    def multiply(x):
        return n * x
    return multiply     # Create a closure multiply_by(n) that multiplies any number by n.
times_by = multiply_by(4)
print(times_by(10))

def add_by(n):
    def add(x):     #Make a closure adder(n) that adds a fixed number n to another number.
        return n + x
    return add
adder = add_by(10)
print(adder(5))


def power_of(n):
    def power(x):     #Write a closure power_func(n) that returns a function to raise numbers to the power n.
        return n ** x
    return power
cube = power_of(3)
print(cube(3))
