list_a = [a for a in range(1,100000)]
list_b = [b for b in range(1,100000)]
#result = [n for n in list_a if n in list_b]
result = [b for b in list_b if b in list_a]


print(result)



