s = input()
s = s.upper()
print("╓" + "─"*(len(s) + 6) + "╖")
print(f"║ F = {s} ║")
print("╙" + "─"*(len(s) + 6) + "╜")
s = s.replace('AND','&')
s = s.replace("XOR", "!=")
z = lambda x : f"#{x}%"
u = lambda x : f"\N{ESC}[38;2;155;255;30m{x}\u001b[0m"
if "D" in s:
    s = s.lower()
    s = s.replace('&','and')
    print(f"\t╔═══╤═══╤═══╤═══╦═══╗\n\t║ A │ B │ C │ D ║ {u('F')} ║\n\t╠═══╪═══╪═══╪═══╬═══╣")
    s1 = (
        "\n".join(
            [
                f"\t║ {a} │ {b} │ {c} │ {d} ║ {z(eval(s))} ║"
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
    print(s1.replace("#","\N{ESC}[38;2;255;255;30m").replace("%", "\u001b[0m"))
    print("\t╚═══╧═══╧═══╧═══╩═══╝")
elif "C" in s:
    s = s.lower()
    s = s.replace('&','and')
    print(f"\t╔═══╤═══╤═══╦═══╗\n\t║ A │ B │ C ║ {u('F')} ║\n\t╠═══╪═══╪═══╬═══╣")
    s1 = (
        "\n".join(
            [
                f"\t║ {a} │ {b} │ {c} ║ {z(eval(s))} ║"
                for a in [0, 1]
                for b in [0, 1]
                for c in [0, 1]
            ]
        )
        .replace("True", "1")
        .replace("False", "0")
        .upper()
    )
    print(s1.replace("#","\N{ESC}[38;2;255;255;30m").replace("%", "\u001b[0m"))
    print("\t╚═══╧═══╧═══╩═══╝")
else:
    s = s.lower()
    s = s.replace('&','and')
    print(f"\t╔═══╤═══╦═══╗\n\t║ A │ B ║ {u('F')} ║\n\t╠═══╪═══╬═══╣")
    s1 = (
        "\n".join([f"\t║ {a} │ {b} ║ {z(eval(s))} ║" for a in [0, 1] for b in [0, 1]])
        .replace("True", "1")
        .replace("False", "0")
        .upper()
    )
    print(s1.replace("#","\N{ESC}[38;2;255;255;30m").replace("%", "\u001b[0m"))
    print("\t╚═══╧═══╩═══╝")