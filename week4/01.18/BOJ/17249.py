import sys
sys.stdin = open("input.txt", "r")

T = list(map(str,input().split('(')))
l = T[0]
r = T[1]
print(l.count('@'), r.count('@'))