#basic calculator
#Input

num1 = int (input("Enter first number"))
num2 = int (input("Enter Second number"))
operator = str (input("Enter operation"))

#calculation
result = 0
if operator == "+":
    result = num1 + num2
    print (result)
if operator == "-":
    result = num1 - num2
    print (result)
if operator == "*" or operator == "x":
    result = num1 * num2
    print (result)
if operator == "/":
    result = num1 / num2
    print (result)
