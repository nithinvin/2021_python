def addDigits(num: int) -> int:
    tnum = num
    sum = 0
    while tnum > 0:
        digit = tnum % 10
        sum = digit + sum
        tnum = int(tnum/10)
        if tnum == 0 and sum > 9:
            tnum = sum
            sum = 0
    return sum

theNum = 8
print("Digit sum is", addDigits(theNum))