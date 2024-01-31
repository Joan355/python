#12. Write a Python program to remove all elements from a given set. 
#Escribe un programa en python que remueva todos los elementos de un set dado

A = set("Este es un conjunto de palabras".split(" "))
print(f"A set size {len(A)}")
A.clear()
print(f"A set size after execting the clear method {len(A)}")
