h = {}
f = open("d8inp.txt", "r")
n = int(f.readline())
print(n)
for _ in range(n):
    row = f.readline().split(" ")
    s, a = row[0].strip(), int(row[1])
    h[s]=a
for _ in range(n):
    s = f.readline().strip()
    if h.get(s):
        print(f'{s}={h[s]}')
    else:
        print("Not found")
