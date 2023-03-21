'''
문제
1. list에 정수 x (x ≠ 0)를 넣는다.
2. list에서 절댓값이 가장 작은 값을 print하고, 그 값을 list에서 제거한다. 
3-1. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 print하고, 그 값을 list에서 제거한다.
프로그램은 처음에 비어있는 list에서 시작하게 된다.

input
1. N(1≤N≤100,000)이 주어진다. 
2. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 
3-1. x가 0이 아니라면 list에 x라는 값을 추가
3-2. x가 0이라면 list에서 절댓값이 가장 작은 값을 print 하고 그 값을 list에서 제거
입력되는 정수는 -231보다 크고, 231보다 작다.

print
입력에서 0이 주어진 회수만큼 답을 출력한다. 
만약 list가 비어 있는 경우인데 절댓값이 가장 작은 값을 print 하라고 한 경우에는 0을 print 하면 된다.'''
import sys 
sys.stdin = open("input.txt", "r")
import heapq

N = int(input())
lst = []
min_lst = []
for _ in range(0,N):
    x = int(input())
    # x가 0이 아니라면 
    if x != 0:
        # x의 음수 양수 여부에 따라 다른list에 추가
        if x < 0:
            heapq.heappush(lst, (abs(x),x))
        else:
            heapq.heappush(lst, (abs(x),x))
    # x가 0이라면 
    else:
        # 음수 list에 값이 있다면/ 음수 list 마지막 값을 출력
        if lst:
            l = heapq.heappop(lst)
            print(l[1])
        # 두 list 모두 비어있다면/ 0을 출력
        else:
            print(0)
            import sys 
sys.stdin = open("input.txt", "r")
import heapq

# N = int(input())
# lst = []
# min_lst = []
# for _ in range(0,N):
#     x = int(input())
#     if x != 0:
#         if x < 0:
#             heapq.heappush(min_lst, x)
#         else:
#             heapq.heappush(lst, x)
#     else:
#         if min_lst:
#             if abs(min_lst[-1]) <= lst[0]:
#                 print(min_lst.pop())
#             elif abs(min_lst[-1]) > lst[0]:
#                 print(heapq.heappop(lst))
#         elif lst:
#             print(heapq.heappop(lst))
#         else:
#             print(0)