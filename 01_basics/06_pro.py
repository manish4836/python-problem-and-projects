a = int(input("enter a number 1: "))
b = int(input("enter a number 2: "))    # find the closest number of the 100

diff_a = abs(100-a)
diff_b = abs(100-b)

if diff_a < diff_b:
    print(a, "is closer  to 100")
else:
    print(b, "is closer to be 100")
