numbers = [1,2,3,4]
numbers_v2 = []
print(numbers)
for i in numbers:
    numbers_v2.append(i * 2)
print(numbers_v2)

numbers_v3 = list(map(lambda i: i * 2, numbers))
print(numbers_v3)

numbers_1 = [i for i in range(1, 5)]
numbers_2 = [i for i in range(5,8)]
print(numbers_1)
print(numbers_2)
result = list(map(lambda x, y : x + y , numbers_1, numbers_2))
print(result)