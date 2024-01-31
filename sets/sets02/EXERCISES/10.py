#10. Write a Python program to check if a set is a subset of another set.
#10. Escribe un programa en python que revise si un conjunto es un subconjunto de otro conjunto
set_A = set("esta es una cadena con alguna palabras".split(" "))
set_B = set("una cadena con alguna".split(" ")) 
print(set_B.issubset(set_A))
print(set_A.issuperset(set_B))