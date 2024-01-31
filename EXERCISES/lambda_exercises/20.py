"""
20. Write a Python program to find the numbers in a given string and store them in a list. Afterward, display the numbers that are longer than the length of the list in sorted form. Use the lambda function to solve the problem.
Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
Numbers in sorted form:
20 23 56

"""

strlist = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5".split(" ")
strlist = [int(num) for num in strlist if num.isdigit()]

result = sorted([x for x in strlist if x > len(strlist)], key= lambda x: x)
print(result)




