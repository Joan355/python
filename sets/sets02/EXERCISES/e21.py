#21. Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type

#21. Escribe un programa en python que encuentre todas las palabras unicas y cuente la frecuencia de ocurrencias de una lista dada de cadenas. Usa sets tipos de datos set

lista = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']

def word_count(words:list[str]) -> dict[str,int]:
    words_set = set(words)
    word_dict = {}
    for word in words_set:
        word_dict[word] = words.count(word)
    return word_dict

if __name__ == "__main__":
    print(word_count(lista))









