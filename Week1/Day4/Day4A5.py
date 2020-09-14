# Assignment: given an array [1,2,3,4,5] write a function that duplicates the array 
# ([1,2,3,4,5,1,2,3,4,5]), you may modify or create a new array.

nums = [1, 2, 3, 4, 5]

def duplicate(array):
    new = array.copy()
    
    for i in new:
        array.append(i)

    print(array)

duplicate(nums)