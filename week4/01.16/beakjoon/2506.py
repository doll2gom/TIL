import sys
sys.stdin = open("input.txt", "r")

T = int(input())
score = list(map(int,input().split()))
cnt = 0
result = 0
for a in score:
    if a == 1:
        cnt += 1
        result += cnt
    elif a == 0:
        cnt = 0
print(result)