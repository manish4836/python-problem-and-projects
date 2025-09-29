def gcd(a, b):   # this is check the common diveder from two values
    gcd_val = 1   # Start with 1 (minimum GCD)
    for i in range(1, min(a, b) + 1):   # Check all numbers till smaller number
        if a % i == 0 and b % i == 0:  #Check if i divides both a and b exactly (remainder 0). If yes, i is a common divisor.
            gcd_val = i
    return gcd_val

print(gcd(8, 12))   # Output: 4
print(gcd(9, 6))    # Output: 3
print(gcd(15, 25))  # Output: 5



# min(a,b ) sechoti vaalue ke niche se lekar 1 tak ke sare number check kar raha hai ki konsa dono value se divide ho raha hai