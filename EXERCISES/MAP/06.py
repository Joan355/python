"""
6. Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use the map() function. 
"""

chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}

result = list(map(lambda x: (x.upper(), x.lower()), chrars))
print(result)