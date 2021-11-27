input_str = input("Enter a string: ")

reversed_str = ""
index = len(input_str)
while index > 0:
    reversed_str = reversed_str + input_str[index - 1]
    index = index -  1

print("Reversed string is: ", reversed_str)

if input_str == reversed_str:
    print("It is a palindrome")
else:
    print("It is NOT a palindrome")
    