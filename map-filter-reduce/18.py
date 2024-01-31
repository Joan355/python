import functools

"""
numbers = [1,2,3,4]
result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)"""
numbers = [1,2,3,4]
def accum(counter, item):
    print("------------------------------")
    print(counter)
    print(item)
    print("------------------------------")
    return counter + item
print(functools.reduce(accum, numbers))
