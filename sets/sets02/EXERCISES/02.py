#2. Write a python program to iterate over sets 
#2. Escribe un programa en python que itere sobre conjuntos (sets)

mysets = [set(palabra) for palabra in "esta es un cadena con palabras".split(" ")]
print(mysets)
#se recorre una lista la cual contiene un cojunto de conjuntos
for i, item in enumerate(mysets):
    for j in item:
        print(f"item -> {j}")
    print(f"fin del conjunto {i + 1}")



    