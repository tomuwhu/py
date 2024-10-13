s = input()
s = s.upper()
s = s.replace("XOR", "!=")
if "C" in s and "D" in s:
    print("A B C D | F")
    s1 = (
        "\n".join(
            [
                f"{a} {b} {c} {d} | {eval(s.lower())}"
                for a in [0, 1]
                for b in [0, 1]
                for c in [0, 1]
                for d in [0, 1]
            ]
        )
        .replace("True", "1")
        .replace("False", "0")
        .upper()
    )
elif "C" in s:
    print("A B C | F")
    s1 = (
        "\n".join(
            [
                f"{a} {b} {c} | {eval(s.lower())}"
                for a in [0, 1]
                for b in [0, 1]
                for c in [0, 1]
            ]
        )
        .replace("True", "1")
        .replace("False", "0")
        .upper()
    )
else:
    print("A B | F")
    s1 = (
        "\n".join([f"{a} {b} | {eval(s.lower())}" for a in [0, 1] for b in [0, 1]])
        .replace("True", "1")
        .replace("False", "0")
        .upper()
    )
print(s1)
