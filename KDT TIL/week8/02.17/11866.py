''' 11866번 요세푸스 문제 0
문제
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

출력
예제와 같이 요세푸스 순열을 출력한다.'''

from collections import deque 

N, K = map(int,input(). split())
K2 = K

lst = [ i for i in range(1,int(N)+1)]
lst = deque(lst)






# 1, 2, 3, 4, 5, 6, 7 // 7(N)%3(K) == 1 // 1,K+1
#                        7//3 == 2
# 1, 2, 4, 5, 7    // 6%3(K)
# 1, 4, 5
'''
<3, 6, 2, 7, 5, 1, 4 >'''

# [1, 2, 3, 4, 5, 6, 7] idx (2) remove
# [1, 2, 4, 5, 6, 7] idx(4) remove
## idx(2) idx(5)
# 6 0 1
# 5 + 3 % len(7)


# [1, 2, 4, 5, 7] 2: idx(1) remove
# [1, 4, 5, 7] 7: idx(3) remove
## idx(1) idx(4)
# 0 1 2
# [1, 4, 5] 5: idx(2) remove
## idx(2)
# 0 1 0
# [1, 4] 1: idx(0) remove
# [4] 4: idx(0) remove
## idx(0) idx(1)


slst = sum(lst)
lst2 = []
ans = []
cnt = 0
while True:
    divmod(len(lst),K2)
    if int(divmod[1]) != 0:
        lst.appendleft(0)
        divmod_result = divmod[0] + divmod[1]

    for k in lst[K-1::K2]:
        ans.append(k)
        cnt += 1

    if len(lst) == cnt:
        break

print(ans)



idx = 0
t = 0
# while True: 
#     # for v in range(len(lst)//K):
#     cnt = 0
#     for k in lst[K-1::K2]:
#         a.append(k)
#         # print(k)
#         # print(lst)
#         # lst.remove(k)
#         # print('22',a)
#         # print(rest)
#         cnt += 1
        
#     # rest = len(lst)%K
#     # K -= rest
#     K = K + K2 * cnt % len(lst)
    
#     idx2 = idx
#     # for mem in a[idx2:]:
#     #     lst.remove(mem)
#     #     idx += 1

#     # print(rest, v)

#     if not lst:
#         break
    
    
#     print(lst)

# print(a)


'''
# while sum(lst) == 0:
def josep(list1,K):
    a = []
    while True:
        for k in list1[K-1::K]:
            a.append(k)
            list1.remove(k)
            list1.append(0)
        if len(list1) == 0:
            break
    return a

for n in josep(lst, K):
    lst2.append(n)
print(lst)
print(lst2)
'''