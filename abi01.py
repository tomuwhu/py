s = input()
print(*[(A, B, C, eval(s)) for A in [0, 1] for B in [0, 1] for C in [0, 1]], sep="\n")
