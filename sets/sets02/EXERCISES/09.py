#9. Write a Python program to create a symmetric difference. 
#9. Escribe un programa en python que cree una diferencia simetrica

set_A = set("esta es una cadena con alguna palabras".split(" "))
set_B = set("esta es la siguiente cadena con algunas palabras repetidas".split(" "))

print(set_A.symmetric_difference(set_B))