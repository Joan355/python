""" Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map. """

numbers = [x for x in range(1, 5)]
result = list(map(lambda x: x**numbers.index(x) , numbers))
print(result)
