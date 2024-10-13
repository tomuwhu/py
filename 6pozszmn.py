k = 100000
v = 999999

def szmcs(s):
    rv = True
    j = 10
    for i in str(s):
        if int(i) >= j:
            rv = False
        j = int(i)
    return rv


print("szmcs")
mo = [s for s in range(k, v + 1) if szmcs(s)]
print(len(mo))

