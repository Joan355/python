#18. Write a Python program to check if a given set is a superset of itself and a superset of another given set.
#18. Escribe un programa en python que revise si un set dado es un  super set de si mismo y un supersert de otro set dado

A = set("Este es un conjunto de palabras".split(" "))# SET DADO
B = set("conjunto de palabras".split(" "))
C = set("conjunto".split(" "))

if A.issuperset(B) and B.issuperset(C):
    print("A es superset de B y B es superset de C")
else: 
    print("A no es superset de B o B no es superset de C")



