list1 = [11, 12, 13, 14, 15]

list1.append(50)
print(list1)

list1.extend([21, 21, 21])
print(list1)

list1.extend("hello")
print(list1)

print(list1.count(21))
