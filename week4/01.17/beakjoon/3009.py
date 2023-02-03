import sys
sys.stdin = open("input.txt", "r")

x1, y1 = list(map(int,input().split()))
x2, y2 = list(map(int,input().split()))
x3, y3 = list(map(int,input().split()))
x_lst = [x1, x2, x3]
y_lst = [y1, y2, y3]
# 하나의 리스트에 정수형태로 모두 넣는다.

lst2 = []
for n in x_lst:
    if x_lst.count(n) == 1:
        lst2.append(n)
for n in y_lst:
    if y_lst.count(n) == 1:
        lst2.append(n)
print(*lst2)