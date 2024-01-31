"""
21. Write a Python program that multiplies each number in a list with a given number using lambda functions. Print the results.
Original list: [2, 4, 6, 9, 11]
Given number: 2
Result:
4 8 12 18 22
"""

num = int(input("Give a number: "))

lista = [2, 4, 6, 9, 11]
result = list(map(lambda x: x * num, lista))
print(result)


