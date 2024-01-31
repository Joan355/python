set_countries = {'col', 'mex', 'bol'} # es un tipo de dato set o conjunto

# tamaño del conjunto
size = len(set_countries)
print(size)

# colombia dentro del conjunto
print("col" in set_countries)

# add   (): set function    

set_countries.add("pe")
print(set_countries)

# update(): set function 

set_countries.update({"arg", "ec", "pe"})
print(set_countries)

# remove(): set function --> remueve del set el elemento especificado
# problema: si se intenta remover un elemento que no existe, lanza exception.
set_countries.remove("col")
print(set_countries)

set_countries.remove("arg") 
print(set_countries)

#set_countries.remove("arg") --> genera error --arg no existe en el set

# discard (): set function --> al igual que remove, remueve el elemento especificado. Sin embargo, no genera error si el elemento a remover o descartar no existe en el set. 

set_countries.discard("arg")

# clear(): set function --> remueve todo del set

set_countries.clear()   
print(set_countries)
print(len(set_countries))

