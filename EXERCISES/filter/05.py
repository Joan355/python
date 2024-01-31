"""Write a Python function that filters out all empty strings from a list of strings using the filter function. """
lista_cadenas = ["", "w3resource", "Filter", "", "Python", ""]
result = list(filter(lambda e: e != "", lista_cadenas))
print(result)
