from functools import reduce

numbers = [i for i in range(1, 5)]

def maxi(it1, it2):
    if it1 > it2:
        return it1
    elif it2 > it1:
        return it2

result = reduce(maxi, numbers) 

print(result)