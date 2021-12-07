list1 = ["harish", "abhinav", "rehan", "sharath", "tirth"]
print (list1)

string = (input("Enter a name: "))
list1.append(string)
print (list1)

num = int(input("Enter a number: "))
print (list1[num])
list1 = [ "Ratul", "Gauri" ] + list1
print (list1)

string2 = (input("Enter a name: "))
if string2 in list1:
    print(string2, "is there")
    list1.remove(string2)
else:
    print(string2, "is not there")
    list1.append(string2)
print (list1)

list2 = list(list1)
list2.reverse()
print ("Reversed list", list2)
print ("Original list", list1)

list1.pop(len(list1) - 1)
print(list1)
