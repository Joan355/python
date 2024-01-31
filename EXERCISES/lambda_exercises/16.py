"""
16. Write a Python program to find the second lowest total marks of any student(s) from the given names and marks of each student using lists and lambda. Input the number of students, the names and grades of each student.
Input number of students: 5
Name: S ROY
Grade: 1
Name: B BOSE
Grade: 3
Name: N KAR
Grade: 2
Name: C DUTTA
Grade: 1
Name: G GHOSH
Grade: 1
Names and Grades of all students:
[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
Second lowest grade: 2.0
Names:
N KAR

"""
#from itertools import takewhile
from itertools import dropwhile
students = [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
result = sorted(students, key= lambda x: (int(x[1]), x[0]))
filtering = list(dropwhile(lambda x: result[0][1] == x[1], result))
print(f"Name:  -> {filtering[0][0]}")
print(f"Grade: -> {filtering[0][1]}")


