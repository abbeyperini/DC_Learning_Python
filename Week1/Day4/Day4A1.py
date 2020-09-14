# Assignment: Write a program which will remove duplicates from the array. 

names = ["Alex","John","Mary","Steve","John", "Steve"]
print(names)

def delete_duplicates(array):
    for n in array:
        times = array.count(n)
        if times > 1:
            index = array.index(n)
            array.pop(index)

delete_duplicates(names)
print(names)

