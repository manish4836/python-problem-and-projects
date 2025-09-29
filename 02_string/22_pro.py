
str1 = input("enter the string 1: ")
str2 = input("enter the string 2: ")
       #Do strings input lo aur check karo ki ek string dusre ka rotation hai ya nahi.
if len(str1) != len(str2):
    print("the string is not rotetional(defferent length)")
elif str2 in (str1+str1):
    print("the string is rotetional")
else:
    print("the string is not rotetional: ")

