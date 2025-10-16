# 'r' - this is read mode 
# 'w' - this is write mode (but purane files delete ho jati hai)
# 'a' - Append mode (nay files  add ho jati hai)
# 'x' - Create mode (nayi file banata hai)

with open('file_01.txt', 'r') as f:   # Only read
    content = f.read()

with open('file_01.txt', 'w') as f:   # Write (overwrite)
    f.write("Naya content\n")

with open('file_01.txt', 'a') as f:   # Append (add at end)
    f.write("Nayi line\n")