
result = [x for x in range(1,101) if any([n for n in range(1,10) if x % n == 0])]
print(result)



