n = 10
a, b = 1, 2
from queue import Queue
q = Queue()
q.put((a, b))
sum = 0
count = 0
t = []
while not q.empty():
    a, b = q.get()
    t.append((a, b))
    if a + b < n:
        q.put((a, a + b))
        q.put((b, a + b))
"t.sort(key = lambda x: x[0] / x[1])"
print(*map(lambda x: f"{x[0]} / {x[1]}", t), sep="\n")