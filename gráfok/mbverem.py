from collections import deque as S
s = S()
pop = s.pop         #verem
#pop = s.popleft    #sor
push = s.append
size = s.__len__
g = {
    1: {'mj':0, 'szl': [2, 3, 4]}, 2: {'mj':0, 'szl': [5, 6]}, 
    3: {'mj':0, 'szl': [7, 8]}, 4: {'mj':0, 'szl': [3, 8, 9]},
    5: {'mj':0, 'szl': [1, 8]}, 6: {'mj':0, 'szl': [5]}, 
    7: {'mj':0, 'szl': [6]}, 8: {'mj':0, 'szl': [9]}, 9: {'mj':0, 'szl': []},
    10: {'mj':0, 'szl': [11]}, 11: {'mj':0, 'szl': [10]}
}
i = 1
p = g[4]
p['mj'] = i
push(p)
while size():
    p = pop()
    for q in p['szl']:
        if g[q]['mj'] == 0:
            i += 1
            g[q]['mj'] = i
            push(g[q])
print(g)