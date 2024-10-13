t = [(5, 1), (8, 7),(9, 9),(11, 6),(7, 3),(3, 9),(2, 4)] # tárgyak listája (méret, fontosság)
wmax = 8 # hátizsák mérete
t.sort(key = lambda x: - x[1] / x[0])
print(t)
hzs = 0
of = 0
for elem in t:
    if elem[0] + hzs <= wmax:
        of += elem[1]
        hzs += elem[0]
        print(hzs, of)
    else:
        mm = (wmax - hzs) / elem[0]
        of += elem[1] * mm
        break
print(of)
