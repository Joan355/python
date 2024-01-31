"""
7. Write a Python program to find if a given string starts with a given character using Lambda.
Sample Output:
True
False
"""

starswithc = lambda string: lambda c: string[0] == c
print(starswithc("String".casefold())("s"))