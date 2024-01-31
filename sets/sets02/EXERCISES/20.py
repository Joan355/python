#20. Write a Python program to remove the intersection of a second set with a first set. 
#2. Escribe un programa en python que remueva la interseccion de un segundo set con un primer set

A = {1,2,3,4,5,6}
B = {5,6,7,8,9,10}

inter = A & B
A = A - inter
B = B - inter
print(A)
print(B)



