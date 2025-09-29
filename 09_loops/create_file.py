name = ("manish is a good boy")

with open("sample.txt","w") as f:  # This will be created a file named sample.txt and write the content in it
    f.write(name)
    print("File created and content written successfully.")

any = open("sample.txt","w")  # This will also create a file named sample.txt and write the content in it
any.write(name)    # any is a variable 
any.close()

with open("sample.txt","r") as f:  # This will read the content of the file named sample.txt
    m = f.read()
    print(m)


with open("sample.txt","a") as f:  # This append will add the content in multiple times
    f.write("\nI am appending this line.")
    print("Content appended successfully.")