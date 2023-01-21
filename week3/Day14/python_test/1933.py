import sys
sys.stdin = open("input.txt", "r")

list = []
T = int(input())
for a in range(1, T + 1):
    if T % a == 0:
        print(a, end=' ')