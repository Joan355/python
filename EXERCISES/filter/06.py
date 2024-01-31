"""Write a Python program that creates a list of dictionaries containing student information (name, age, grade) and uses the filter function to extract students with a grade greater than or equal to 95. 

Escribe un programa en python que cree una lista de diccionarios que contengan informacion de estudiantres (name, age, grade) y use la funcion filter para extraer studiantes con una nota mayor o igual a 95

"""

students = [
    {"name": "Denis Helio", "age": 17, "grade": 97},
    {"name": "Hania Mehtap", "age": 16, "grade": 92},
    {"name": "Kelan Stasys", "age": 17, "grade": 90},
    {"name": "Velvet Mirko", "age": 16, "grade": 94},
    {"name": "Delores Aeneas", "age": 17, "grade": 100},
]

GRADE = 95

result = list(filter(lambda element: element["grade"] >= GRADE, students))
print(result)


