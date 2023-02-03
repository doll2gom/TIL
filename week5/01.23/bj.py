import sys 
sys.stdin = open("input.txt", "r")
import heapq

N = int(input())
lst = []
min_lst = []
for _ in range(0,N):
    x = int(input())
    if x != 0:
        if x < 0:
            heapq.heappush(min_lst, x)
        else:
            heapq.heappush(lst, x)
    else:
        if min_lst:
            if abs(min_lst[-1]) <= lst[0]:
                print(min_lst.pop())
            elif abs(min_lst[-1]) > lst[0]:
                print(heapq.heappop(lst))
        elif lst:
            print(heapq.heappop(lst))
        else:
            print(0)