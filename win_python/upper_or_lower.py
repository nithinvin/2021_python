input_str = input("Enter a string: ")

if input_str.isupper():
    print(input_str, "is an upper case string")
    print("Now it is a lower case string:", input_str.lower())
else:
    print(input_str, "is an lower case string")
    print("Now it is an upper case string:", input_str.upper())