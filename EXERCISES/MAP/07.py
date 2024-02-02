"""
7. Write a Python program to add two given lists and find the difference between them. Use the map() function
"""

nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]

result = list(map(lambda x,y: (x + y , x - y), nums1, nums2))
print(result)