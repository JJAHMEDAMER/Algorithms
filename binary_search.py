def binary_search(list, target):
    left = 0
    right = len(list)-1
    while right >= left:
        i = (left + right)//2  # Floor Operator // 
        if list[i] == target: 
            return i
        elif list[i] < target:
            left = i + 1
        else:
            right = i - 1


list = [1,2,3,4,5,6,7,8,9]

index = binary_search(list, 9)
print(index, len(list))


"""
Binary Search Big O 
O(Log N)
"""
