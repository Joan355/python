set_countries = {"col", "mex", "bol"}
size = len(set_countries)

print(size)

print("col" in set_countries)
print("pe" in set_countries)

#add 
set_countries.add("pe")
set_countries.add("pe")
set_countries.add("pe")
set_countries.add("pe")
print(set_countries)

#update

set_countries.update(["pe", "ecua", "ar", 2])
print(set_countries)

#remove

set_countries.remove("col")
print(set_countries)

set_countries.remove("ar")
print(set_countries)

set_countries.clear()
print(set_countries)
