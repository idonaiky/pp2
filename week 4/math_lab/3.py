import math
def f():
    n=float(input())
    l=float(input())
    p=n*l
    k=math.radians(180/n)
    a=l/2*math.tan(k)
    print(p*a/2)
f()