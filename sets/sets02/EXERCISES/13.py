#13. Write a Python program that uses frozensets.
#Note: Frozensets behave just like sets except they are immutable

#13. Escribe un programa en python que use 


mydict = {k:len(k) for k in "Esto es un conjunto de palabras".split(" ")}
my_frozen_set = frozenset(mydict)
for k in my_frozen_set:
    print(mydict[k])

