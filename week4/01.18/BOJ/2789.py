import sys
sys.stdin = open("input.txt", "r")

cbg = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

lst =[]
T = str(input())
Tl = len(T)
for t in range(0,Tl):
    w = T[t]
    if cbg.count(w) == 0:
        lst.append(T[t])
for l in lst:
    print(l,end='') 