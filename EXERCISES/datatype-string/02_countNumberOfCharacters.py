"""Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}"""

text = "Este es un texto complemente inventado con el fin de evaluar el funcionamiento de este programa"
count = {c: text.count(c) for c in text}
print(count)
