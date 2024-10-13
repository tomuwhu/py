n = int(input())
f = n * (n + 1) // 2
h1 = []
h2 = []
if f % 2:
    print("NO")
else:
    print("YES")
    c = f // 2
    for i in range(n, 0, -1):
        if i <= c:
            h1.append(i)
            c -= i
        else:
            h2.append(i)
    print(len(h1))
    print(*h1)
    print(len(h2))
    print(*h2)

