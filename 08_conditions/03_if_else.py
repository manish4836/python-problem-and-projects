is_male = True
if is_male:
    print("You are a male.")

is_female = False
if is_female:
    print("You are a female.")


is_male = False # ek hi true hona chahiye
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both.")
else:
    print("You are neither male or tall.")



is_male = True # dono valu e true hona chahiye
is_tall = False
if is_male and is_tall:
    print("You are a tall male.")
else:
    print("You are either not male or not tall.")


is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not(is_tall):   # not is_tall means is_tall = False then print this
    print("You are a short male.")
elif not(is_male) and is_tall:   # not is_male means is_male = False then print this
    print("You are not male but you are a tall.")
else:
    print("You are not a male or not tall or both.")