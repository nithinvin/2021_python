num = int(input("Enter a number: "))

tnum = num
sum = 0
while tnum > 0:
    digit = tnum % 10
    tnum = int(tnum/10)
    sum = sum + digit

print ("The sum of the digits is: ", sum)