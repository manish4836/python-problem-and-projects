sentence = input("enter the sentence: ")

words = sentence.split()
                             # count the no. of words in the sentennce
count = 0

for word in words:
     count = count + 1
    
print("the no. of words in a sentence is: ", count)




sentence = input("Enter the sentence: ")          #this is the another method
print("The number of words:", len(sentence.split()))
