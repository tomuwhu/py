def dld(s1, s2):
    l1, l2, d = len(s1), len(s2), {}
    for i in range(-1, l1 + 1): 
        d[(i, -1)] = d[(-1, i)] = i + 1
    for i in range(l1):
        for j in range(l2):
            c = 0 if s1[i] == s2[j] else 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,      # deletion
                d[(i, j - 1)] + 1,      # insertion
                d[(i - 1, j - 1)] + c,  # substitution
            )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i, j)], d[i - 2, j - 2] + c) # transposition
    return d[l1 - 1,l2 - 1]
print(dld('jézuska','géppuska')) #3