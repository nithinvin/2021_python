print("Enter the nine numbers row-wise: ")
row_1 = []
row_2 = []
row_3 = []

i = 0
while i < 3:
    row_1.append(int(input()))
    i += 1

i = 0
while i < 3:
    row_2.append(int(input()))
    i += 1

i = 0
while i < 3:
    row_3.append(int(input()))
    i += 1

print(row_1)
print(row_2)
print(row_3)

sum1 = 0
for item in row_1:
    sum1 += item
print(sum1)

sum2 = 0
for item in row_2:
    sum2 += item
print(sum2)

sum3 = 0
for item in row_3:
    sum3 += item
print(sum3)