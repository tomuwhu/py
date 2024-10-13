i = float('inf')
a = 10
w = [
    [0, 6, 2, 5, i, a, 9],
    [1, 0, i, i, i, 3, i],
    [i, i, 0, 2, a, i, 4],
    [5, i, 2, 0, 2, i, 8],
    [i, i, a, 2, 0, i, 2],
    [a, 3, i, i, i, 0, 3],
    [9, i, 4, 8, 2, 3, 0]
]
t = w[:]
n = len(w)
for k in range(n):
    for j in range(n):
        for i in range(n):
            t[i][j] = min(t[i][j], t[i][k] + t[k][j])
print(' ', *range(1, n + 1))
for y, row in enumerate(t):
    print(y + 1, *map(lambda x: "A" if x > 9 else x, row))
