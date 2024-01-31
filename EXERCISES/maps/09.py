"""Write a Python program to compute the square of the first N Fibonacci numbers, using the map function and generate a list of the numbers."""

def fibonacci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[:n]

def square(n):
    return n*n

result = list(map(square, fibonacci(6)))
print(result)