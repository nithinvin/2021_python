string = input("Enter a sentence: ")
word_count = 1
for char in string:
    if char == " ":
        word_count += 1

print ("The number of words in the string is ", word_count)