"""numbers = []

for element in range(1, 11):
    numbers.append(element * 2)

print(f"resultado de la lista: {numbers}")

numbers = [element * 2 for element in range(1,11)]
print(f"resultado de la lista: {numbers}")
"""
numbers = []

for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i * 2)

print(f"resultado de la lista: {numbers}")


#usando list comprehension

numbers_v2 = [i * 2 for i in range(1, 11)  if i % 2 == 0]
print(f"resultado de la lista: {numbers_v2}")













