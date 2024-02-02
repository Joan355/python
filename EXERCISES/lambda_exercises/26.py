"""
26. Write a Python program to find a list with maximum and minimum length using lambda.
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])
"""
lista = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

result = [(len(r),r) for r in [max(lista, key=lambda i: len(i)), min(lista, key= lambda i: len(i))]]
print(result)

