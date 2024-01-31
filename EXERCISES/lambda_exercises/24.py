"""
24. Write a Python program to find numbers within a given range where every number is divisible by every digit it contains.
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

"""
myrange = range(1,23)

result = list(
    filter(
        lambda x: all(
            map(
                lambda n: int(n) != 0 and x % int(n) == 0
                ,str(x)))
        ,myrange))
print(result)

