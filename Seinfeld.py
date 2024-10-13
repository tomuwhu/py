from itertools import count
import sys
sys.stdin = open("ANARC09A.txt") # Seinfeld
def f(sx):
    x = ''
    for i in sx:
        if i == "{" or i == "}": x += i
    k = x.count("{")
    v = x.count("}")
    return abs(k - v)
v = input()
s = 0
while v[0] != "-":
    s += 1
    print(f"{s}. {f(v.strip())}")
    v = input()
