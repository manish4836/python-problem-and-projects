sentence = input("enter a sentence: ")
      #Reverse each word in a sentence
words = sentence.split()

rev = []
for word in words:

   rev.append(word[ ::-1])
result = " ".join(rev)

print(result)

