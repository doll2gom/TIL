import sys
sys.stdin = open("input.txt", "r")

lst = []
for n in range(1,10):
    number = int(input())
    lst.append(number)
m = max(lst)
print(f'{m}\n{lst.index(m)+1}')