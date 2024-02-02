"""
10. Write a Python program to compute the square of the first N Fibonacci numbers, using the map function and generate a list of the numbers. 
"""
from functools import reduce 
N = 10 
fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

# 0 1 1 2 3 5 8 