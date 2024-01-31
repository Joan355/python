import functools 
#[0,1,2,3,5,8,13, ...]
result = lambda n: functools.reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0,1])
n = 10
print(f"La sucesion de fibonacci para {n} es: {result(n)}")