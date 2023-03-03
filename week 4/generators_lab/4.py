import math
def f(x, y):
    n = x
    while n <= y:
        yield n ** 2
        n += 1

a = int(input())
b = int(input())
for i in f(a, b):
    print(i)