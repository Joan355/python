"""4. Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map"""

bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

zipped = zip(bases_num,index)
result = list(map(lambda x: x[0]**x[1], zipped))
print(result)
