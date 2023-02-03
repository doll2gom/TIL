import sys
sys.stdin = open("input.txt", "r")

lst = []
while True:
    a, b = map(int,input().split())
    if a != 0 and b != 0:
        lst.append(a + b)
    elif a == 0 and b == 0:
        break
for n in lst:
    print(n)