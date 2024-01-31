"""Write a Python program that creates a list of names and uses the filter function to extract names that start with a vowel (A, E, I, O, U)."""

list_of_names = ["Elita", "Vitold", "Audovacar", "Kerensa", "Ramana", "Iolanda", "Landyn"]
vocals : tuple [str]= ("A","E","I","O","U")
result = list(filter(lambda n: n[0].upper() in vocals, list_of_names))
print(result)