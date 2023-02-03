import sys
sys.stdin = open("input.txt", "r")

numbers = []
T = int(input())
for n in range(1,T+1):
    n = int(input())
    if n not in numbers:
        numbers.append(n)
    numbers.sort()
# 뭔가 리스트 컴프리헨션으로 구현이 가능할 것 같은데, 아직은
for number in numbers:
    print(number)
