# Assignment: Assume you're suppose tp have an array of 10 integers from 0-9. One number is missing. Write a function that will determine the missing element.

integers = [0, 1, 2, 3, 4, 5, 6, 7, 9]

def whats_missing(array):
    ten_ints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    miss_ints = []

    for i in ten_ints:
        if i in array:
            continue
        else:
            miss_ints.append(i)


    print(f"You're missing {miss_ints}.")


whats_missing(integers)