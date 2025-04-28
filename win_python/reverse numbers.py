num = int(input("Enter a number : "))

rnum = 0
tnum = num
while tnum > 0:    
    digit = tnum % 10    
    tnum = int(tnum/10)    
    rnum = (rnum * 10) + digit    

print ("The reversed number is : ", rnum)