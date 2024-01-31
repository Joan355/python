lista_a = [1,2,3,4,5,6,7,8,9]
lista_b = [2,7,1,12]
result = [(a,a) for a in lista_a if a in lista_b]
print(result)