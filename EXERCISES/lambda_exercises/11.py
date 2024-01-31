"""
11. Write a Python program to find the intersection of two given arrays using Lambda.
Original arrays:
"""

intersection = lambda arr1, arr2: set(arr1).intersection(arr2)
arr1 = {1,2,3,4,5}
arr2 = {3,4,5,6,7}

print(intersection(arr1,arr2))
