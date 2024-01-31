
A = "Hola"

def getPopulation():
    keys = ["Colombia", "Bolivia"]
    values = [300,400]
    return keys,values

def getPopulationByCountry(data, country):
    result = list(filter(lambda item : item["Country"].lower() == country.lower(), data))
    return result