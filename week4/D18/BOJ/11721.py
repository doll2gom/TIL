import sys
sys.stdin = open("input.txt", "r")

W = str(input())
l_W = len(W)
w = l_W//10

for n in range(0,w+1):
    print(W[n*10:(n+1)*10:1])