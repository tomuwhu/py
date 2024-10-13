[TOC]

# Python példaprogramok

## 9. évfolyam

### 38. óra - Egyenletmegoldás ciklussal

- Newton iteráció (kiegészítő anyag)
TK. 117. (1.e. megoldás)

```python
fx = lambda x: 2*x**3 - 3*x + 1
Df = lambda x: 6*x**2 - 3
xn = 0
for n in range(0,10):
    print(xn) # Megoldásközelítés az n. iterációban.
    xn = xn - fx(xn)/Df(xn)
# https://secure.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/
```

### 41. óra - Listák és bejárásuk

- Összegzés
TK. 124. - 125.

```python
f = open("inut.txt","r")
z = 0
for i in f.read().split("\n"):
    z += int(i)
print(z)
```

- 5-ös lottó nyerőszám generátor példaprogram

```python
from random import shuffle # a keverés(shuffle) importálása
li = [ *range( 1, 90 ) ]   # vegyük a számokat 1-től 90-ig
shuffle( li )              # keverjük össze a sorrendjüket
lo = li[ :5 ]              # vegyük az első 5-öt (ez az 5 nyerőszámunk)
lo.sort(    )              # rendezzük őket növekvő sorrendbe
print ("Az 5 nyerőszám:")
for la in lo:
    print(la)              # írjuk ki a képernyőre őket
```

## 10. évfolyam

### ??. óra - Függvények alkalmazása

- Hanoi tornyai
TK. 61.

```python
def h(n, a, b):
    if ( n == 1 ):
        return "( {} => {} )".format(a, b)
    else: 
        return (
            h( n-1, a,     6-a-b )+
            h( 1,   a,     b )+
            h( n-1, 6-a-b, b )
        )
print( h( 3, 1, 2 ) )
```
