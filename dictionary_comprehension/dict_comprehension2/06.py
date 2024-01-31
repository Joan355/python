import random 
countries = {"col","mex","bl","pe"}
population = {country : random.randint(0,1000) for country in countries}
result = {country:pop for country,pop in population.items() if pop > 500}
print(result)

text = "Hola, soy Joani."
unique = {c:c.upper() for c in text if c in "aeiou"}
print(unique)

