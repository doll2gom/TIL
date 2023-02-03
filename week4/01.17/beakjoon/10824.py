import sys
sys.stdin = open("input.txt", "r")

a, b, c, d = input().split()
print(int(a + b) + int(c + d))