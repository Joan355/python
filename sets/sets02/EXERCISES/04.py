#  Write a Python program to remove item(s) from a given set. 
# Escribe un programa en python para remover items de un set dado

myset = set("estos son elementos de mi set".split(" "))

# remove estos
myset.difference_update({"estos", "elementos"})
print(myset)


