#17. Write a Python program to check if two given sets have no elements in common. 
#17. Escribe un programa en python que revise si dos sets dados no tienen ningun elemento en comun

A = set("Este es un conjunto de palabras".split(" "))
B = set("Este es un conjunto de palabras inventadas y pues estos es todos, gracias".split(" "))

inter = A.symmetric_difference(B)
if len(inter) == 0:
    print("The given sets have no elements in common")
else: print(f"The given sets don't have {len(inter)} elements in common")


