from math import pi, sqrt, sin

def fakt(x):
    f = 1
    for i in range(1, x + 1): f *= i
    return f

def ssin(x):
    s = 0
    for n in range(0, 50):
        s += (-1)**n * x**(2*n + 1) / fakt(2*n + 1)
    return s

def nsin(x):
    return f"{ssin(x):.8g}"

def rsin(x):
    return f"{sin(x):.8g}"

def gy(x):
    return f"{sqrt(x):.8g}"

print(*map(rsin, [0, pi/6, pi/2, 3*pi/2, pi/3, pi/4]))
print(*map(nsin, [0, pi/6, pi/2, 3*pi/2, pi/3, pi/4]))
print(*map(gy, [0, 1/4, 1, 400, 3/4, 1/2]))