import csv

def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter= ",")
        header = next(reader)
        data = []

        for row in reader:
            iterable = zip(header, row)
            country_dict = {key:value for key, value in iterable}
            data.append(country_dict)
    return data




data = read_csv("C:/Users/alexa/Downloads/archive/world_population.csv")
country = list(filter(lambda e: e["Country/Territory"] == "Andorra", data))
print(country[0]["2022 Population"])
