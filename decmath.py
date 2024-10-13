from decimal import *
import math
print( Decimal(math.pi) )
print( Decimal(127/17) )

from fractions import Fraction
print(
    Fraction(31,17), "*", Fraction(19, 21), "+", Fraction(2, 3), "=", 
    Fraction(31,17) * Fraction(19, 21) + Fraction(2, 3)
)

from itertools import count
x = count()
while (a:=next(x))<15: print(a)

x = count(1,3)
y = count(6,2)
a = 0
b = 1
while a<b:
    a, b = next(x), next(y)
    print(a, b)
