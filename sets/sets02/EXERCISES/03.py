#Write a python program to add members to a set

set_A = set("Esta es una cadena de ejemplo".split(" "))
set_B = set(", y esta es otra cadena que extiende a la primera".split(" "))
set_A.add("PALABRA")
print(set_A)
set_A.update(set_B)
print(set_A)



