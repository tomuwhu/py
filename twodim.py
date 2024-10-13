print(
    [list(range(10*i,10*i+10)) for i in range(10)]
)
print("-----")
print(
    list(map(lambda x: list(range(x*10,x*10+10)),range(10)))
)