"""5. Write a Python program to square the elements of a list using the map() function. """

numbers = range(1,10)
result = list(map(lambda x: x**2, numbers))
print(result)