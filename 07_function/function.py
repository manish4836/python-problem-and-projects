# def cal_fac(n):
#     fact = 1
#     for i in range (1 , n +1):
#         fact *= i
#     print(fact)
# cal_fac(5)
# cal_fac(10)

#convert doller into the rupees
'''def converter(usd_val):
    inr_val = usd_val* 88.1735
    print(f"{usd_val} usd = {inr_val} INR ")
converter(100)

'''
def val_check(num):
    if num %2 == 0:
        print("the value is even.")
        return True
    else:
        print("the value is not even.")
        return False
val_check(6)


