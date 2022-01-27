def isHappy(n: int) -> bool:
    tnum = n
    squared_sum = 0
    while tnum > 0:
        digit = tnum % 10
        squared_sum = (digit ** 2) + squared_sum
        tnum = int(tnum/10)
        if tnum == 0:
            if squared_sum == 1:                
                return True
            elif squared_sum == 4:                
                return False
            else:
                tnum = squared_sum
                squared_sum = 0

def printHappyOrNot(n: int, happy: bool):
    if happy:
        print(n, "is happy")
    else:
        print(n, "is not happy")


mynum = 124
printHappyOrNot(mynum, isHappy(mynum))
