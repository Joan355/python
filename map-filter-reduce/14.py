numbers = [1,2,3,4]
"""numbers_v2 = []
for i in numbers:
    numbers_v2.append(i*2)
print(numbers_v2)"""

numbers_v3 = list(map(lambda n: n*2, numbers))
print(numbers_v3)

numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7]
result = list(map(lambda x,y: x + y, numbers_1, numbers_2))
print(result)
