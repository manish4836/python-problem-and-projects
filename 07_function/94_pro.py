def fabonach(num):
    if num == 0 :
        return 0
    elif num == 1:
        return 1
    else:
        return fabonach(num -1) + fabonach(num - 2)


print(fabonach(10))