rf = ["and", "not", "xor", "or"]
s = input().lower()
so = s.upper()
for i, v in enumerate(rf): s = s.replace(v, str(i))
try:
    vl = list(map(lambda x: f"{x}", filter(lambda x: x in s, "abcdefghijklmnoprstuvwxyz")))
    for i, v in enumerate(rf): s = s.replace(str(i), v).replace('xor', '!=')
    print(f"Q = {so}")
    l = eval(f"""[[{", ".join(vl)}, eval(s)] {" ".join(map(lambda x: f"for {x} in [False, True]", vl))}]""" )
    for row in sum([[sum([list(map(lambda x: x.upper(), vl)), ["Q"]], [])], l], []):
        print("\t" * 5, "|" .join(map(str, row)) .replace("True", "I").replace("False", "H"))
except: print("Hibás kifejezés!")
