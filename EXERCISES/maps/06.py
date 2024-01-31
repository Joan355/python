"""Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use the map() function."""

def convertToUL(c: str):
    return (c.upper(), c.lower())


seq = "Esta es una secuencia de caracteres".replace(" ","")
result = list(map(convertToUL, seq))
print(result)


