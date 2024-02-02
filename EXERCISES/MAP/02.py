"""
2. Write a Python program to add three given lists using Python map and lambda. 
"""

list1 = range(1,10)
list2 = range(10,20)
list3 = range(20,30)
result = list(map(lambda x,y,z: x + y + z, list1,list2, list3))
print(result)