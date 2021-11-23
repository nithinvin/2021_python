num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Select an operator [ + - * / %]: ")

invalid_operator = 0
result = 0
if (op == "+"):
    result = num1 + num2
elif (op == "-"):
    result = num1 - num2
elif (op == "*"):
    result = num1 * num2
elif (op == "/"):
    result = num1 / num2
elif (op == "%"):
    result = num1 % num2
else:
    print ("Invalid operator")
    invalid_operator = 1
    exit

if invalid_operator == 0:
    print (num1, op, num2, "=", result)

