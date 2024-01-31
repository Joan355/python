#7. Write a Python program to create a union of sets. 
#7. Escribe un programa en python que cree una union de conjuntos

set_A = set("esta es una cadena con alguna palabras".split(" "))
set_B = set("esta es la siguiente cadena con algunas palabras repetidas".split(" "))

print(set_A | set_B)