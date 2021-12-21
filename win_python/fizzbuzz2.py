def fizz_buzz(input):
    return_string = ""
    if input%3 == 0:
        return_string = "Fizz"

    if input%5 == 0:
        return_string += "Buzz"

    if return_string == "":
        return_string = input

    return return_string
    

print(fizz_buzz(25))