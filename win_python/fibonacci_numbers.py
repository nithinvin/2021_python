num = int(input("Enter how many fibonacci numbers you want: "))

num1 = 0
num2 = 1
print (num1, num2, end=" ")
printed_num = 2
current_num = 0
while printed_num != num:
    current_num = num1 + num2
    print (current_num, end=" ")
    num1 = num2
    num2 = current_num
    printed_num = printed_num + 1
