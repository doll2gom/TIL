import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for n in range(1,T+1):
    number = int(input())
    numbers = list(map(int,input().split()))
    print(sum(numbers))