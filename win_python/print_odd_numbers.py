N = int(input("Enter a number: "))

sum = 0
for oddnum in range(1,N + 1,2):
    sum = oddnum + sum

print(sum, "is the sum of odd numbers till", N)