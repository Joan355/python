"""Write a Python program that creates a list of tuples, each containing a city name and its population. Use the filter function to extract cities with a population greater than 2 million

Escribe un programa en python que cree una lista de tuplas, cada una conteniendo el nombre de una ciudad y su poblacion. Usa la funcion filter para extraer las ciudades con una poblacion mayor a 2 millones. 
"""
import random

cities = [
    ("New York", 8500000),
    ("Los Angeles", 4000000),
    ("Chicago", 2700000),
    ("Houston", 2300000),
    ("Phoenix", 1600000),
    ("Philadelphia", 1500000),
    ("San Antonio", 1500000),
]

result = list(filter(lambda city: city[1] > 2000000, cities))
print(result)


