num = int(input("Enter a number:"))
fact = 1
n = num
while n>0:
    fact = fact * n
    n = n - 1
print ("The factorial of", num, "is", fact)
