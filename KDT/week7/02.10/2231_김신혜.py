''' 2231번 분해합
A의 분해합은 N(A과 A을 이루는 각 자리수의 합)
A의 분해합이 B인 경우, B을 A의 생성자라 한다.

A(245) -> N(256(=245+2+4+5))분해합
A(245)생성자 <- N(256)

A -> N(분해합)
A(생성자) <- N

생성자가 없을 수도, 생성자가 여러 개인 자연수도 있을 수 있다.
자연수 N(분해합)이 주어졌을 때, B의 가장 작은 생성자(A) 구하기

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

출력
첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.'''
"""216"""
#198
'''
100의 자리의 경우 
숫자의 길이는 3이되고 각 자리마다 9가 들어갔을 때 최댓값을 제외하여 계산하기로 한다. 
999 (999+9+9+9)
'''
'''from collections import deque
lst = deque()    # 분해합 후보 리스트
lst2 = deque()   # 분해합에 대당하는 리스트
N = int(input())
for _ in range(N):
    # 탐색할 정수(생성자 후보)를 10으로 나누면서 몫과 나머지를 구한다.
    lst.append(N)
    a = divmod(N, 10)
    if a[0] == 0:
        break
    lst.append(a)
    print(a)
    a = a[0]
    # 나머지를 리스트에 담는다.
    # 몫은 다시 탐색할 숫자로 변경

    # 몫이 0이 될때까지 반복하여 나머지를 계속해서 리스트에 모은다.
    # 몫이 0이 나오면 break 
    
    # lst 속의 숫자의 합이 원래 입력값과 완전히 동일하다면 
    # 가장 앞에 있는 인덱스[0]의 수가 생성자에 해당하기 때문에 두번째 리스트에 모아둔다.
        # print('3 : ', n, lst)

print(sorted(lst2)[0])    # 두번째 리스트에서 가장 작은 생성자를 출력'''

import sys
from collections import deque
lst = deque()
N = int(sys.stdin.readline())
for n in range(N,1,-1):   
    for _ in n:
        print(n)
        cnt = [n]
        n1 = n//10
        if n1 == 0:
            break
        n2 = n%10
        print(n1, n2)
        cnt.append(n2)
        n = n1
    if sum(cnt) == N:
        lst.append(cnt[0])
    print(sorted(lst))
# print(sorted(lst2)[0]) 