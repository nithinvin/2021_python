def plusOne(digits: list[int]) -> list[int]:
    int_string = ""
    for digit in digits:
        int_string = int_string + str(digit)
    actual_integer = int(int_string) + 1
    ret_list = []
    for char in list(str(actual_integer)):
        ret_list.append(int(char))
    return ret_list

    


myInteger = [1, 2, 9, 9]
retInteger = plusOne(myInteger)

print(retInteger)