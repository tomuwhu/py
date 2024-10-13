n = 10
def f(a, b):
    global n
    yield f"{a}/{b}"
    if a + b < n:
        yield from f(a, a + b)
        yield from f(b, a + b)
print(*f(1, 2))