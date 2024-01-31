"""Write a Python program to convert a given list of integers and a tuple of integers in a list of strings. """

list1 = [1,2,3,4,5]
tuple1 = (1,2,3,4,5)

resultlist = list(map(str, list1))
resulttuple = list(map(str, tuple1))
