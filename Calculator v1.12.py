print(" ###   ###  #      ###  #   # #      ###  #####  ###  ####")
print("#   # #   # #     #   # #   # #     #   #   #   #   # #   #")
print("#     ##### #     #     #   # #     #####   #   #   # ####")
print("#   # #   # #     #   # #   # #     #   #   #   #   # #   #")
print(" ###  #   # #####  ###   ###  ##### #   #   #    ###  #   #")
print("")
print("")
print("             Welcome to Calculator v1.12")
print("                Created by Abdulla      ")
print("                     ©2024        ")
print("")
def calc():
    print("Choose operation:|+| |-| |*| |/| |**|")
    a = input()
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
        print("Enter first number: ")
        x = float(input())
        print("Enter second number: ")
        y = float(input())
        print("Answer is:", x / y)
    elif a == "**":
        print("Enter number: ")
        x = float(input())
        print("Enter number's exponent: ")
        y = float(input())
        print("Answer is:", x ** y)
    else:
        print("Wrong operation!")
        global cont
    cont = input("Continue? Y/any key for N: ")

calc()

if cont == "Y":
    while cont:
        calc()
        if cont == "N":
            print("Bye!")
            break