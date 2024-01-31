""" Write a Python function that filters out even numbers from a list of integers using the filter function."""
"""https://www.w3resource.com/python-exercises/filter/index.php"""

def evenFilter(x):
    return x % 2 == 0

numbers = [x for x in range(1, 101)]
result = list(filter(evenFilter,numbers))
print(result)
