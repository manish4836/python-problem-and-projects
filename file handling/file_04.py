# file = open("file_01.txt", "w")
# file.write("this is my new line. \n")
# file.write("file handling mast chiz hai.\n")
# file.close

with open("file_01.txt", "w") as files:
    files.write("this is good.\n")
    files.write("this is helpful for read and write the code")
    files.closed