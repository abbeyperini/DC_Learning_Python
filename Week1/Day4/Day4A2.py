# Assignment: Write a program which finds the largest element in the array 

words = ["apple", "banana", "orange", "apricot", "supercalifragilisticexpialidocious"]
numbers = [1, 4, 23, 103, 567, 1432, 40523, 1000000]

def find_largest(array):
    length = 0
    item = ""

    for n in array:
        if len(str(n)) > length:
            length = len(str(n))
            item = n
   
    print(item)


find_largest(words)
find_largest(numbers)