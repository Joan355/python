#14. Write a Python program to find the maximum and minimum values in a set. 
#14. Escribe un programa en python para encontrar el valor maximo y minimo en un set

from random import randint

values = [randint(1,20) for i in range(1,20)]
set_values = set(values)
print(f"max value from set values {max(set_values)}")
print(f"min value from set values {min(set_values)}")