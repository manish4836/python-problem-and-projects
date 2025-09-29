counter = 0
def increament_counter():   #def function ke andar variable ko change karne ke liye usse global declare karna padta hai
    global counter
    counter = counter + 1
    
print("before function call",counter)
increament_counter()
print("after first call", counter)
increament_counter()
print("after second call", counter)
increament_counter()
print(counter)
increament_counter()
print(counter)
increament_counter()