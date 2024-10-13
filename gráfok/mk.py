g = {
    1: {'szl': [2, 3, 4]}, 2: {'szl': [5, 6]}, 
    3: {'szl': [7, 8]}, 4: {'szl': [3, 8, 9]},
    5: {'szl': [1, 8]}, 6: {'szl': [5]}, 
    7: {'szl': [6]}, 8: {'szl': [9]}, 9: {'szl': []},
    10: {'szl': [11]}, 11: {'szl': [10]}
}
i = 0
def mb(p):
    global i
    g[p]['u'] = i
    i += 1
    [mb(q) for q in g[p]['szl'] if not 'u' in g[q]]
    g[p]['v'] = i
    i += 1
for i in g: if not 'u' in g[i]: mb(i)
gt = {}
for i in g: gt[i] = {'szl': []}
for i in g:
    for j in g[i]['szl']:
        gt[j]['szl'].append(i)
        gt[j]['u'] = 0
gtl = []
for i in g:
    gtl.append({'p': i, 'szl': g[i]['szl'], 'v': g[i]['v']})
gtl.sort(key = lambda x: -x['v'])

def mb2(p):
    global dsz
    dsz += 1
    gt[p]['u'] = 1
    print(p, end=" ")
    [mb2(q) for q in gt[p]['szl'] if not gt[q]['u']]

for i in gtl:
    dsz = 0
    if not gt[i['p']]['u']: mb2(i['p'])
    if dsz: print()
