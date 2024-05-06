
# Simple Calculator

num1 = float(input("Type the first number: "))
num2 = float(input("Type the second number: "))
oper = input("Type the operator: ")

print(num1, oper, num2)


if oper == "+": 
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "*":
        print(num1 * num2)
elif oper == "/":
        print(num1 / num2)
else:
    print("Invalid operator !!")
