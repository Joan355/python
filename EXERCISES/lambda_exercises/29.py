"""
29. Write a Python program to find the maximum value in a given heterogeneous list using lambda.
Original list:
['Python', 3, 2, 4, 5, 'version']
Maximum values in the said list using lambda:
5
"""
heter_list = ['Python', -4, -3,-2, -1, 'version']
_max = max(heter_list, key= lambda x: (isinstance(x,str), x))

print(_max)