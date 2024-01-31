string = "Find all of the words that are less than 4 letters".split(" ")
result = [s for s in string if len(s) < 4]
print(result)