file = open("./text.txt")
#print(file.read())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())

for line in file:
    print(line)

file.close()  # al cerrar el flujo entre el archivo y el programa, libera espacio de memoria. 


with open("./text.txt") as file:
    for line in file: 
        print(line)