print(*[2**(i-1)*(2**i-1) for i in [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127]], sep="\n")
from random import randrange as r
def sb(r, g, b):
     print(f'\N{ESC}[48;2;{r};{g};{b}m')
def rgb(s, r, g, b):
    return f'\N{ESC}[38;2;{r};{g};{b}m{s}\u001b[0m'
print(rgb("Meglepetés szín",r(50,256), r(50,256), r(50,256)))
sb(r(256), r(256), r(256))
print(rgb("Meglepetés szín",r(50,256), r(50,256), r(50,256)))