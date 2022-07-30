def linear_search(list, target):
    """
    Return the position or index of the value we are searching for
    """
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return -1


list = [1,2,3,4,5,6,7,8,9]

index = linear_search(list, 9)
print(index, len(list))

"""
len list returns the number of items in a list starting from 1
range start from fist argument to the last argument -1 
    range(0, 9) 0 -> 8
"""