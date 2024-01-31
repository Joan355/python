"""
4. Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

"""
r = lambda x: x["color"]

list_dicts = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

result = sorted(list_dicts, key=r, reverse=True)

print(result)

