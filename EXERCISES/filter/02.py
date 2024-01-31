""" Write a Python program that uses the filter function to extract all uppercase letters from a list of mixed-case strings"""


text = "EsTE Es UN teXTo coN LetRaS De DIfereNTEs TamanoS".split(" ")
result = map(lambda c : list(filter(lambda char : char.isupper(), c)), text)
print(list(result))
#result_v2 = [lista for r in result for lista in r]
#print(result_v2)



