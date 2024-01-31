"""Write a Python function that filters out all elements less than or equal than a specified value from a list of numbers using the filter function."""

numbers = [20, 15, 24, 37, 23, 11, 7]
value = 20
result = list(filter(lambda n : n <= value, numbers))
print(result)

