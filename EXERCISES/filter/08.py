"""Write a Python program that creates a list of words and use the filter function to extract words that contain more than five letters. 

Escribe un programa en python que cree una lista  de palabras y use la funcion filter para extraer palabras que contienen mas de cinco letras

"""

text = "Escribe un programa en python que cree una lista de palabras  y use la funcion filter para extraer palabras que contienen mas de cinco letras".replace("  ", " ").split(" ")


result = list(filter(lambda word : len(word) > 5 , text))
result_v2 = list(filter(lambda word : len(word) <= 5 , text))
print(f"Plabras con mas de cinco letras -> {result}")
print(f"Plabras con menos de cinco letras -> {result_v2}")
