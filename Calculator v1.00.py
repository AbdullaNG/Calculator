print(" ###   ###  #      ###  #   # #      ###  #####  ###  ####")
print("#   # #   # #     #   # #   # #     #   #   #   #   # #   #")
print("#     ##### #     #     #   # #     #####   #   #   # ####")
print("#   # #   # #     #   # #   # #     #   #   #   #   # #   #")
print(" ###  #   # #####  ###   ###  ##### #   #   #    ###  #   #")
print("")
print("")
print("             Welcome to Calculator v1.00")
print("                Created by Abdulla      ")
print("                     ©2024        ")
print("")

print("Choose operation:|+| |-| |*| |/| |**|")
a = input()
try:
    if a == "+":
        print("Enter first number: ")
        x = float(input())
        print("Enter second number: ")
        y = float(input())
        print("Answer is:", x + y)
    elif a == "-":
        print("Enter first number: ")
        x = float(input())
        print("Enter second number: ")
        y = float(input())
        print("Answer is:", x - y)
    elif a == "*":
        print("Enter first number: ")
        x = float(input())
        print("Enter second number: ")
        y = float(input())
        print("Answer is:", x * y)
    elif a == "/":
        try:
            print("Enter first number: ")
            x = float(input())
            print("Enter second number: ")
            y = float(input())
            print("Answer is:", x / y)
        except ZeroDivisionError:
            print(x)
            while True:
                print('-0                       (ctrl + c) to exit!')
    elif a == "**":
        print("Enter number: ")
        x = float(input())
        print("Enter number's exponent: ")
        y = float(input())
        print("Answer is:", x ** y)
    else:
        print("Wrong operation!")
except ValueError:
    print('Invalid value!')
print("Press Enter to exit!")
j = input()