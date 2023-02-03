# import sys
# sys.stdin = open("input.txt", "r")

input_numers = '2 1 5 3 4'
input_numers = list(map(int,input().split()))
wood = input_numers

# 풀이 1
while wood != [1, 2, 3, 4, 5]:
    for n in range(0,4):
        if wood[n] > wood[n+1]:
            a = wood[n]
            wood.remove(a)
            wood.insert(n+1,a)
            print(*wood)
# 풀이 2
while True:
    for n in range(len(wood)-1):
        if wood[n] > wood[n+1]:
            wood[n], wood[n+1] = wood[n+1], wood[n]
            print(wood)

    if wood == [1, 2, 3, 4, 5]:
        break
