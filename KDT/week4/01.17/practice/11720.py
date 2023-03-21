import sys
sys.stdin = open("input.txt", "r")

T = int(input())
numbers = str(input())
n = 0
for number in numbers[0:T+1]:
    n += int(number)
print(n)