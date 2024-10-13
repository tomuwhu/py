n = int(input())
l = []
for i in range(n):
    l.append([i, int(input())])
l.sort(key = lambda x: -x[1])
i = 0
h = 0
o = []
while l:
    q = l.pop()
    while q[1] > h:
        i += 1
        h += len(str(i))
    s = list(reversed(list(str(i))))
    o.append([q[0], s[q[1]-h]])
o.sort(key = lambda x: x[0])
print(*[i[1] for i in o], sep="\n")