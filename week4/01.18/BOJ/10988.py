import sys
sys.stdin = open("input.txt", "r")

T1 = str(input())
T2 = T1

if T1[:] == T2[::-1]:
    print(1)
else:
    print(0)