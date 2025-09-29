list = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
rotetion = list[-k:] + list[:-k] #Rotate a list by k positions (e.g., [1,2,3,4,5] rotated by 2 → [4,5,1,2,3]).
print(rotetion)