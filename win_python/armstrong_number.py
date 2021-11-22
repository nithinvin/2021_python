num = int(input("Enter a number: "))
tnum = num
sum = 0
while tnum > 0:
    digit = tnum % 10
    sum = (digit ** len(str(num))) + sum
    tnum = int(tnum/10)
if num == sum:
    print (num, "is an armstrong number")
else:
    print (num, "is not an armstrong number")