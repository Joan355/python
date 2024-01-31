def increment(x):
    return x + 1

increment_v2 = lambda x : x + 1
result =  increment(10)
print(result)
result = increment_v2(20)
print(result)

full_name = lambda name, lastname : f'Full name es {name.title()} {lastname.title()}' # el metodo .title() capitaliza el una cadena
text = full_name("joan", "salazar")
print(text)

