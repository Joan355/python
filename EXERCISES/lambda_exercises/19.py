"""
18. Write a Python program to find palindromes in a given list of strings using Lambda.
Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']
"""
"""
words = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
palindromes = list(filter(lambda x: x == "".join(reversed(x)), words))
print(palindromes)"""


