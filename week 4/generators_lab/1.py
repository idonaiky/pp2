import math
def f(max):
    n = 1
    while n <= max:
        yield n ** 2
        n += 1

n = int(input())
for i in f(n):
    print(i)