"""
13. Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
Original arrays: [1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5
"""
arr = [1, 2, 3, 5, 7, 8, 9, 10]
count_Even = len(list(filter(lambda x: x % 2 == 0, arr)))
count_Odd = len(list(filter(lambda x: x % 2 != 0, arr)))

print(f"Number of even numbers in the abouve array: {count_Even}")
print(f"Number of odd numbers in the abouve array: {count_Odd}")
