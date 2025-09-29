def sort_list(number):
    return sorted(number , key = lambda x : x % 10)    # last digit ke hisaab se sort kar raha hai
numbers = [22, 43, 44, 56, 76, 78, 99]

sorted_list = sort_list(numbers)
print(sorted_list)