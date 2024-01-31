#16. Write a Python program to check if a given value is present in a set or not. 
#16. Escribe un programa en python que revise si un valor dado esta presente es el set o no

A = set("Write a Python program to check if a given value is present in a set or not.".split(" "))
value = input("check if a given element is present in the set -> ")
if value in A:
    print(f"The element ´{value}´ is in the set A")
else: print(f"The element ´{value}´ is not un the set A")
