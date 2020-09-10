def is_number(input_num):
    try:
        input_num = int(input_num)
        return True
    except ValueError:
        print("Whoops! That is not a valid integer.")

def check_prime():
    number = input("Give me an integer between 2 and 100: ")
    
    if is_number(number):
        num = int(number)
        remainders = []

        if num < 2 or num > 100:
            check_prime()
        else:
            for i in range(2, num):
                remainder = num % i
                remainders.append(remainder)

        if 0 in remainders:
            print("Not prime.")
        else: 
            print("Prime!")
    else:
        check_prime()
        
check_prime()