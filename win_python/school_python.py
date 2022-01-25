string_input = (input("Enter a sentence: "))
vowel_count = 0

for char in string_input:
    if char.lower() in ["a", "e", "i", "o", "u"]:
        vowel_count += 1

    
print ("number of vowels is : ", vowel_count)

