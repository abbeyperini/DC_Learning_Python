first = input("Enter your first number: ")
operand = input("Enter your operand: ")
second = input("Enter your second number: ")

def addition(first, second):
    add = int(first) + int(second)
    return add

def subtration(first, second):
    sub = int(first) - int(second)
    return sub

def multiplication(first, second):
    mult = int(first) * int(second)
    return mult

def division(first, second):
    div = int(first) / int(second)
    return div
    
if operand == '+':
    add_print = addition(first, second)
    print(add_print)
elif operand == '-':
    sub_print = subtration(first, second)
    print(sub_print)
elif operand == '*':
    mult_print = multiplication(first, second)
    print(mult_print)
elif operand == '/':
    div_print = division(first, second)
    print(div_print)
else:
    print("Please provide a valid operand (+, -, *, /).")


def even_odd():
    number = input("Give me a number, any number: ")
    num = int(number)
    if num % 2 == 0:
        print("This number is even.")
    else:
        print("This number is odd.")

even_odd()


def fizz_buzz():
    number = input("Give me a number > 0! ")
    num = int(number)
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 3!= 0 and num % 5 == 0:
        print("Buzz")
    else:
        print("No fizzes or buzzes for you.")

fizz_buzz()
