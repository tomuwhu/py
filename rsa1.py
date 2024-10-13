from random import randrange as rr

def blnko( a, b ):
    if b == 0:
        return (a, 1, 0)
    else:
        d, x, y = blnko( b, a % b )
        return ( d, y, x - (a // b) * y )

def lkm(a,b,n):
    print("most")
    d, x, y = blnko( a, n )
    if d % b != 0:
        x *= ( b // d ) % n
        for i in range(d):
            y = x + i * (n / d) % n
            if b * y % n == 1:
                d = y
                break
    return d

def cp(a, b):
    while b != 0:
        a, b = b, a % b
    return a==1

p = 11
q = 13

m = 9

n = p * q
fn = ( p - 1 ) * ( q - 1 )

while True:
    e = rr(2,fn)
    if cp( e, fn ):
        break

d = lkm(e,1,n)

print( f'n = {n}, fn = {fn}') 
print( f'e = {e}, d = {d}, e * d = {( e * d ) % fn}' )

print( m )

a = m
for i in range( fn ):
    a = ( a * m ) % n

print( a )

