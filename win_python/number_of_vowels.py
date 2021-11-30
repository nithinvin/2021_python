string = input("Enter a sentence: ")
vowel_count = 0
vowels = "aeiou"
for char in string:
    if char in vowels:
        vowel_count += 1

print ("The number of vowels in the string is ", vowel_count)
