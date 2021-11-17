my_list = ['siya', 'Tiya', 'Guru', 'Piya', 'jiya', 'diya', 'Guru']

i = 0

while True:
    if (i == len(my_list)):
        break
    if (my_list[i] == 'Guru'):
        print("Skipping an interesting name")
        i += 1
        continue
    print("Current name is", my_list[i])
    i += 1

print("After exiting while loop")