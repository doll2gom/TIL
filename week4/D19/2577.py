import sys
sys.stdin = open("input.txt", "r")

from collections import Counter

A = int(input())
B = int(input())
C = int(input())
X = str(A*B*C)

for n in range(0,10):
    N = str(n)
    if N in Counter(X):
        print(Counter(X).get(N))
    else:
        print(0)