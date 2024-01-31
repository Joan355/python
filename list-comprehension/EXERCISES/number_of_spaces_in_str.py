string = "Esta es una cadena que cuenta con una cantidad de n espacios"
result = [i for i in string if i.isspace()]
print(len(result))