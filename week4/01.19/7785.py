import sys
sys.stdin = open("input.txt", "r")

N = int(input())
ent = {}
lst = []

for n in range(0,N):
    name, status = input().split()
    if status == 'enter':
        ent[name] = status
    else:
        del ent[name]

for i in ent:
    lst.append(i)
lst.sort()
lst.reverse()

print(*lst, sep='\n')