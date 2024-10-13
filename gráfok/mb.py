g = {
    1: {'szl': [2, 3, 4]}, 2: {'szl': [5, 6]}, 
    3: {'szl': [7, 8]}, 4: {'szl': [3, 8, 9]},
    5: {'szl': [1, 8]}, 6: {'szl': [5]}, 
    7: {'szl': [6]}, 8: {'szl': [9]}, 9: {'szl': []},
}
def mb(p):
    g[p]['mj'] = 1
    print(p)
    [mb(q) for q in g[p]['szl'] if not 'mj' in g[q]]
mb(1)
print(g)