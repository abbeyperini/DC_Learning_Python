def is_number(input_num):
    try:
        input_num = int(input_num)
        return True
    except ValueError:
        print("Whoops! That is not a valid number.")

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

def calculator():
    first = input("Enter your first number: ")
    operand = input("Enter your operand: ")
    second = input("Enter your second number: ")
    
    if is_number(first) and is_number(second):
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
            calculator()
    else:
        print("Please provide a valid number.")
        calculator()

calculator()

def even_odd():
    number = input("Give me a number, any number: ")
    if is_number(number):
        num = int(number)
        if num % 2 == 0:
            print("This number is even.")
        else:
            print("This number is odd.")
    else:
        print("Please provide a valid number.")
        even_odd()

even_odd()


def fizz_buzz():
    number = input("Give me a number from 1 - 99! ")
    if is_number(number):
        num = int(number)
        if num == 0 or num > 99:
            fizz_buzz()
        elif num % 3 == 0 and num % 5 == 0:
            print("Fizz Buzz")
        elif num % 3 == 0 and num % 5 != 0:
            print("Fizz")
        elif num % 3!= 0 and num % 5 == 0:
            print("Buzz")
        else:
            print("No fizzes or buzzes for you.")
    else:
        print("Please provide a valid number.")
        fizz_buzz()

fizz_buzz()
