"""
14. Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda.
Sample Output:
Monday
Friday
Sunday
"""

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

result = list(filter(lambda word: len(word) == 6, weekdays))
print(result)