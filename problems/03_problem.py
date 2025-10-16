def sum_digits(n):
    num = int(input("Enter the number: "))
    total = 0
    for digit in str(num):
        total += int(digit)
    return total

print(sum_digits(12345))  # Output: 15

def sum_digit(n):
    return sum(int(digit) for digit in str(n))
print(sum_digit(12345))  # Output: 15