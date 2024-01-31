#5. Write a Python program to remove an item from a set if it is present in the set.
#5. Escribe un programa en python para remover un item de un conjunto si esta presente en el set

myset = set("estos son elementos de mi set".split(" "))

# remove estos
myset.discard("estos")
print(myset)
