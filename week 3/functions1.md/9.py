import math
def volume_of_sphere(r):
    return 4/3*r**3*math.pi
r = float(input())
print(volume_of_sphere(r))