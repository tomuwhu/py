import sys
sys.stdin = open("ANARC09A.txt") # Seinfeld
def f(sx):
    x = ''
    for i in sx:
        if i == "{" or i == "}": x += i
    i = 0
    ix = 0
    jx = 0
    j = len(x) - 1
    r = 0
    while i <= j:
        if x[i] == "{": ix += 1
        else: ix -= 1
        if x[j] == "}": jx += 1
        else: jx -= 1
        if ix < 0:
            ix = 0
            r += 1
        if jx < 0:
            jx = 0
            r += 1
        i += 1
        j -= 1
    return r + abs(ix - jx) // 2
v = input()
s = 0
while v[0] != "-":
    s += 1
    print(f"{s}. {f(v.strip())}")
    v = input()
