"""Write a Python program to square the elements of a list using the map() function. """

def square(element):
    return element*element

numbers = [x for x in range(1,11)]
result = list(map(square, numbers))
print(result)