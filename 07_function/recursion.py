def show(n):
    if (n==0) :
        return 
    print(n)
    print("END")
    show(n-1)
show(6)



def fact(n):
    if n ==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))


def fact(n):
    if n ==0 or n==1:
        return 1
    return n *fact(n-1)
print(fact(5))


def cal_sum(n):
    if n ==0 :
        return 0
    print(n)
    return cal_sum(n-1) + n

print(cal_sum(5))