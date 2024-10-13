import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()

for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

con.close()

print("ff=%.2f, kd='%s'" % (2.23455, 'cica'))
print("ff=%6.2f, kd='%6s'" % (2.23455, 'cica'))

for i in range(32, 127):
    print("A '%c' karakter kódja: %d" % (i, i))