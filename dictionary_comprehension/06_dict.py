import random 

countries  =["col" , "mex" , "bol", "pe"]
population = {country : random.randint(1,100) for country in countries }
print(population)

result = { country : pop for country , pop in population.items() if pop > 20}
print(result)

text = "Hola, soy Joan."
unique = {c: c.upper() for c in text if c in "aeiou"}
print(unique)
