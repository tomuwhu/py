def h(n,a,b,c):
    if n==1:
        print(a,c)
    else:
        h(n-1,a,c,b)
        print(a,c)
        h(n-1,b,a,c)
n = int(input())
print(2 ** n - 1)
h(n, 1, 2, 3)