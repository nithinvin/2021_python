def isPrimeNumber(n):
    j = 2
    while j<=(n ** 0.5):        
        if (n%j == 0):
            return True
            break
        j = j + 1
    if (j>(n ** 0.5)):
        return True
    n = n + 1

def isUgly(n: int) -> bool:
    if n <= 0:
        return False
    if n == 1:
        return True
    if ((n % 2) != 0) and ((n % 3) != 0) and ((n % 5) != 0):
        return False
    tnum = n
    while ((tnum % 2) == 0):
        tnum = tnum / 2
    while ((tnum % 3) == 0):
        tnum = tnum / 3
    while ((tnum % 5) == 0):
        tnum = tnum / 5
    if tnum == 1:
        return True
    if isPrimeNumber(tnum):
        return False
    else:
        return True

num = 968
print("For", num, "isUgly returns", isUgly(num))