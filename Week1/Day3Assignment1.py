def is_number(input_num):
    try:
        input_num = int(input_num)
        return True
    except ValueError:
        print("Whoops! That is not a valid integer.")

def factorial():
    number = input("Enter an integer: ")
    
    if is_number(number):
        num = int(number)
        just_nums = []
        total = num

        for i in range((num - 1), 0, -1):
            just_nums.append(i)
    
        for i in range(0, len(just_nums)):
            total *= just_nums[i]
    
        print(total)
    
    else:
        factorial()

factorial()