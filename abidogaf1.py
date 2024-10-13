a, n = 7, 20
for i in range(1, n):
    print(a)
    a += 3 if a%2 else a // 2
