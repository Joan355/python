import random 
"""countries = ["col","mex", "bl", "pe"]
population = {country : random.randint(1,100) for country in countries}
print(population)"""


names = ["nico","zule","santi"]
ages = [12,56,98]
new_dict = {name : age for name,age in zip(names,ages)}
print(new_dict)
