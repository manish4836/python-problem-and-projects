sentence = "Python is easy to learn and Python is powerful"  #count the each word how much time 
words = sentence.split()  # Split sentence into words

word_count = {}  # Empty dictionary to store counts

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)