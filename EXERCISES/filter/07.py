"""Write a Python program that filters out prime numbers from a list of integers using the filter function. 
    Escribe un programa en python que filtre los numeros primos de una lista de enteros usando la funcion filter
"""
import timeit

setup_code = """
numbers = [i for i in range(1, 200)]
primes = {2, 3, 5, 7}

def primeNumber(number):
    if number in primes:
        return True
    
    for i in primes:
        if number % i == 0:
            return False
    
    if number != 1:
        primes.add(number)

    return True
"""

stmt_code = """
result = list(filter(primeNumber, numbers))
"""

# Ejecutar timeit
execution_time = timeit.timeit(stmt=stmt_code, setup=setup_code, number=10000)

print(f"Tiempo de ejecución: {execution_time} segundos")

