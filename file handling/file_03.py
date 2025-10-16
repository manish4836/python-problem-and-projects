file = open("file_01.txt", "r")   # r means read the file 
content = file.read()
print(content)
file.close()

with open("file_02.py", "r") as file:
    content = file.read()
    print("file ka content")
    print(content)
    
