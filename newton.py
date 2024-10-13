fx = lambda x: 2*x**3 - 3*x + 1
Df = lambda x: 6*x**2 - 3
xn = 0
for n in range(0,10):
    print(xn) # Megoldás az n. iterációban.
    xn = xn - fx(xn)/Df(xn)
# forrás:
# https://secure.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/