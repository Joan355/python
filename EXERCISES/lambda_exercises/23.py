"""
23. Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using the lambda function.
Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
Sum of the positive numbers: -32
Sum of the negative numbers: 48
"""
numbers = [2, 4, -6, -9, 11, -12, 14, -5, 17]
positive = sum(filter(lambda x: x > 0, numbers))
negative = sum(filter(lambda x: x < 0, numbers))
print("Sum of the positive numbers: {}".format(positive))
print("SUm of the negative numbers: {}".format(negative))
