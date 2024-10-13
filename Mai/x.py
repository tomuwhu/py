t = [7,4,3,7,2,1,3,4,3]
t.sort(key = lambda x: -x)
print(*map(lambda x: x**2, t))