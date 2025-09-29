def c_vovels(string):
    vowels = "aeiou"
    count = 0
    for ch in string:
        if ch in vowels:
            count += 1
    print(count)
c_vovels(input("enter the string: "))