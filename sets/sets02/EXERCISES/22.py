#22. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value
from functools import reduce
nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = 35

def findpairfromtarget(nums:list[int]) -> set[tuple]:
    #{(),(),(),()}
    nums = set(nums)
    pairs = set()
    for num in nums:
        complement = target - num
        if complement in nums:
            pairs.add((num,complement))
        
    return pairs

print(findpairfromtarget(nums))


