"""
Caracteristicas de los sets:

* No permiten duplicados
* son mutables o se pueden modificar
* No tienen orden

"""

# conjuntos de palabras

set_countries = {'col', 'mex', 'bol'} # es un tipo de dato set o conjunto
set_countries.add("chile")
print(set_countries)
print(type(set_countries))

# conjuntos de numeros

set_numbers = {1,2,3,4,5,5,6,7,7}
print(set_numbers)

# conjuntos de tipos 

set_types = {1, "palabra", False, 12.2}
print(set_types)

# conjunto creado a partir de un string

set_from_string = set("hoola")
print(set_from_string)

# crear conjunto a partir de una tupla

set_from_tuple = set(("abc", "cbv", "as", "abc"))
print(set_from_tuple)

# crear tupla a partir de una lista

numbers = [1,3,45,2,2,3,4,5,3,1,2,2,3,4,5,6,8]
set_numbers = set(numbers)
print(set_numbers)

unique_numbers = list(set_numbers)
print(unique_numbers)


