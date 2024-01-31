#19. Write a Python program to find elements in a given set that are not in another set. 
#19. Escribe un programa en python que encuentre elementos en un set dado que no esten en otro set

A = {1,2,3,4,5,6}
B = {4,5,6,7,8,9}
dif1 = A - B
dif2 = B - A 
print(dif1)
print(dif2)