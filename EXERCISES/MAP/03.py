"""
3. Write a Python program to listify the list of given strings individually using Python map.
"""
strlist = "3. Write a Python program to listify the list of given strings individually using Python map.".split(" ")
result = list(map(lambda x: list(x), strlist))
print(result)