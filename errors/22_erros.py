
try:
    print(0/0)
except ZeroDivisionError as error:
    print("Error")

try:
    assert 1 != 1, "Uno no es diferente de uno"
except AssertionError as error:
    print(error)

print("Hola")