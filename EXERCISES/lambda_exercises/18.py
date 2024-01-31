"""
19. Write a Python program to find all anagrams of a string in a given list of strings using Lambda.
Orginal list of strings:
['bcda', 'abce', 'cbda', 'cbea', 'adcb']
Anagrams of 'abcd' in the above string:
['bcda', 'cbda', 'adcb']

"""
from collections import Counter

strings = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
givenstr = "abcd"
result = list(filter(lambda x: Counter(givenstr) == Counter(x), strings))
print(result)



