set_A = {"col","bol","mex"}
set_B = {"bol","pe"}


result_union = set_A.union(set_B)
print(result_union)
result_union = set_A | set_B
print(result_union)

result_intersection = set_A.intersection(set_B)
print(result_intersection)
result_intersection = set_A & set_B

result_difference = set_A.difference(set_B)
print(result_difference)
result_difference = set_A - set_B
print(result_difference)

result_symmetric_difference = set_A.symmetric_difference(set_B)
print(result_symmetric_difference)
result_symmetric_difference = set_A ^ set_B
print(result_symmetric_difference)
