"""Write a Python program to add two given lists and find the difference between them. Use the map() function. """
def diflist(l1, l2):
    return (l1 + l2, l1 - l2)

list1 = [1,2,3,4,5,6,7]
list2 = [2,5,2,7,4,6,8]
result = list(map(diflist, list1, list2))
print(result)