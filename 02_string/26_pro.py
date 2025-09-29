sentence = input("enter the sentence : ")
words = sentence.split()
longest = ""            # find the longest word of the sentence

for word in words:
    if len(word)>len(longest):
        longest = word
print("the longest word is:", longest)

# htis is another short method


sentence = input("enterr the sentence: ")
print("the longest word is: ", max(sentence.split(),key=len))

# the sortest word in the sentence


sentence = input("Enter the sentence: ")
words = sentence.split()

shortest = words[0]   # pehle word se start karte hain

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("The shortest word is:", shortest)

#this is another method


sentence = input("Enter the sentence: ")
print("The shortest word is:", min(sentence.split(), key=len))

