num = 4
while num<100:
    j = 2
    while j<=(num ** 0.5):
        #print ("Check if", num, "is divisible by", j)
        if (num%j == 0):
            #print (num, "is not a prime number")
            break
        j = j + 1
    if (j>(num ** 0.5)):
        print (num, "is a prime number")
    num = num + 1
