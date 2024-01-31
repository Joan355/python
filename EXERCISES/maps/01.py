"""Write a Python program to triple all numbers in a given list of integers. Use Python map. """
"""https://www.w3resource.com/python-exercises/map/index.php"""
numbers = [x for x in range(1, 11)]
result = list(map(lambda x: x*3, numbers))
print(result)