from decimal import Decimal as D

digit_1 = D(input("Please enter first digit: "))

math_operation = input("Please enter operation (+, -, *, /): ")

digit_2 = D(input("Please enter second digit: "))

if math_operation == "+":
    result = digit_1 + digit_2
elif math_operation == "-":
    result = digit_1 - digit_2
elif math_operation == "*":
    result = digit_1 * digit_2
elif math_operation == "/":
    if digit_2 == 0:
        print("Division by zero error!")
    result = digit_1 / digit_2
else:
    print("Error")

print("Result:", D(result))
