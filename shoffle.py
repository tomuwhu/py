from random import shuffle
li = [ *range( 1, 90 ) ]
shuffle( li )
lo = li[ :5 ]
lo.sort(    )
print ("Az 5 nyerőszám:")
for la in lo:
    print(la)