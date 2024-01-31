"""11. Write a Python program to create a shallow copy of sets.

Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object. """

"""
11. Escribe un programa en python que cree una copia superficial de conjuntos

Nota: una copia superficial es una copia bit a bit de un objeto. Un nuevo objeto es creado, el cual tiene una copia exacta de los valores en el objeto original

"""
"""
class Person:
    def __init__(self, name, age) -> None:
       self.name = name 
       self.edad = age


    def __hash__(self) -> int:
        print(f"Hashing {self.name}...")
        return sum([ord(i) for i in self.name]) + self.edad
    
    def __eq__(self, __value: object) -> bool:
        print(f"Comparando {self.name} con {__value.name} ...")
        return  True if self.name ==__value.name and self.edad == __value.edad else False
    
    def __str__(self) -> str:
        return (self.name, self.edad)

p2 = Person("alex",22)
p1 = Person("joan",22)
p3 = Person("naoj",22)
p4 = Person("jose",22)
p5 = Person("jose",22)

myset = {p3,p5,p1,p4,p2}
for i in myset:
    print(i.name,i.edad)"""

from copy import deepcopy
class Person:
    def __init__(self, name, age) -> None:
       self.name = name 
       self.edad = age


    def __hash__(self) -> int:
        print(f"Hashing {self.name}...")
        return sum([ord(i) for i in self.name]) + self.edad
    
    def __eq__(self, __value: object) -> bool:
        print(f"Comparando {self.name} con {__value.name} ...")
        return  True if self.name ==__value.name and self.edad == __value.edad else False
    
    def __str__(self) -> str:
        return (self.name, self.edad)

p1 = Person("joan",22)
p2 = Person("alex",23)
p3 = Person("jose",21)
p4 = Person("nicolas",21)

set_personas = {p1,p2,p3,p4}
set_copia = deepcopy(set_personas)

for i in set_personas:
    print(i.name)

print("-----------------------------")

for i in set_copia:
    print(i.name)


print("-----------------------------")

for i in set_copia:
    i.name = "Alexander"
    break

print("-----------------------------")

for i in set_personas:
    print(i.name)

print("-----------------------------")

for i in set_copia:
    print(i.name)


