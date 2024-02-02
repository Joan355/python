"""
1. Write a Python program to triple all numbers in a given list of integers. Use Python map. 
"""

numbers = range(1,100)
result = list(map(lambda x: x*3, numbers))
print(result)