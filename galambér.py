osszeg = 0
db = 0
l = [2.6, 1.3, 0.2, 5.17, 6, 7.8, 3.48, 1.9, 11.9, 1, 12.23, 1.1, 2]
for (i, v) in enumerate(l):
    print(f"{i + 1}. csomag: {v} kg.", end="")
    if v < 2:
        osszeg += v
        db += 1
        print("!", end="")
    print()
print(f"összeses csomag tömege: {osszeg}")
print(f"csomag száma: {db} ")
print(f"kézbesített csomagok átlagos tömege: {osszeg/db}")
