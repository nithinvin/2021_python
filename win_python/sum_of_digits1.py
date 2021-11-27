num = input("Enter a number: ")

sum = 0
for char in num:
    sum = sum + int(char)

print("The sum of digits is: ", sum)