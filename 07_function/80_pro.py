#  This is the function method
def calc_fact(num):   # find the factorial of the number
    fact = 1
    for i in range (1, num + 1):
        fact *= i
    print(fact)
    
calc_fact(9)


# this is the loop method

n= int(input('enter the number: '))
result = 1
for i in range(1, n + 1):
    result *= i

print(result)