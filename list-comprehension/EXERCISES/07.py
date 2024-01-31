string = "In 1984 there were 13 instances of a protest with over 1000 people attending".split(" ")
result = [n for n in string if n.isnumeric()]
print(result)