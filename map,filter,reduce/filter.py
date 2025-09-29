l = [4, 8, 15, 16, 50]
def  filter_function(x):
    return x>= 15
new_list = list(filter(filter_function, l))
print(new_list) 
# filter() ye pure list, tuple ,etc in me se kuch elements ko filter krta hai based on condition jo hum dete hain
# filter() me hum function dete hain our fir vo jo value true hoti hai vo values outputme print krta hai