"""

15. Write a Python program to add two given lists using map and lambda.
Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9]
"""

arr1 = [1,2,3]
arr2 = [4,5,6]

result = list(map(lambda x,y: x + y, arr1, arr2))

print(f"Result; after adding two list\n{result}")

