def h(n, a, b):
    if ( n == 1 ):
        return "( {} => {} )".format(a, b)
    else: 
        return (
            h( n-1, a,     6-a-b )+
            h( 1,   a,     b )+
            h( n-1, 6-a-b, b )
        )
print( h( 4, 1, 2 ) )
