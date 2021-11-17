my_list = ['siya', 'Tiya', 'Guru', 'Piya', 'jiya', 'diya', 'guru']

i = 0

while True:
    print(my_list[i])
    if (my_list[i] == 'Piya'):
        print("Found the name Piya")
        break
        print("After break statement")
    i += 1

print("After exiting while loop")