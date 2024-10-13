def x(*a):
    return ", ".join(map(str, sorted(a)))
print(
    x(3, 5, 2, 7, 9)
)
