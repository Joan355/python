""" Write a Python function that filters out elements from a list of strings containing a specific substring using the filter function

Escribe una funcion de python que filtre elementos de una lista de cadenas que contengan una sub cadena especifica, usando la funcion filter

"""

text = "Escribe una funcion de python que filtre elementos de una lista de cadenas que contengan una sub cadena especifica, usando la funcion filter".replace(",","").split(" ")

specific_substring = "fi"

def getElementsWithSubs(element):
    return specific_substring in element

result = list(filter(getElementsWithSubs, text))
print(result)