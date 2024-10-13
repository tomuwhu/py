l = [str(x) for x in input().split(" ")]
t = l[0]
tantargyak = l[1:]
n = int(input())
kik = [[] for i in range(len(tantargyak))]
for i in range(n):
    y = [str(x) for x in input().split(" ")]
    szam = i + 1
    for j in y:
        if j in tantargyak:
            kik[tantargyak.index(j)].append(szam)
for i in kik:
    print(len(i), end=" ")
    print(*i)
