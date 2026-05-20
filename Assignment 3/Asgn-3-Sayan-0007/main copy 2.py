with open("Assignment 3/Asgn-3-Sayan-0007/Supervised.txt", "r") as file:
    text = file.read()
text = text.lower()
words = text.split()
word_count = {}
for word in words:
    
    if word in word_count:
        word_count[word] += 1
    
    else:
        word_count[word] = 1

print(word_count)