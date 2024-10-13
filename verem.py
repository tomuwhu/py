sp = 0
mem=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def push(a):
    global sp, mem
    mem[sp] = a
    sp+=1
def pop():
    global sp, mem
    sp-=1
    return mem[sp]

push('A')
push('B')
push('C')
print(sp)
print(mem) 

print(pop())
print(mem)
print(sp)

push('E')
push('F')
push('G')
print(sp)
print(mem) 