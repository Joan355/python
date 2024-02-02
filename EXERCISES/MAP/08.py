"""
8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings. 
"""

nums_list = [1, 2, 3, 4]
nums_tuple = (0, 1, 2, 3)

result1 = list(map(lambda x: str(x), nums_list))
result2 = list(map(lambda x: str(x), nums_tuple))
result1.extend(result2)
print(result1)
