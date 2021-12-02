list1 = [19, 31, 22, 9]
sum = 0
list_len = len(list1)

for num in list1:
    sum = sum + num
    
mean = sum/list_len

print ("The sum of numbers is: ", sum)
print ("The mean of the numbers is: ", mean)