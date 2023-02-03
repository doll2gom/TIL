'''문제
A에서 한 자리를 뽑고 * B에서 임의로 한 자리를 뽑아 곱한다.
의 가능한 모든 조합 (A가 n자리, B가 m자리 수라면 총 가능한 조합은 n*m개)을 더한 수로 정의하려고 한다.

예를 들어 121*34는
1*3 + 1*4 
+ 2*3 + 2*4 
+ 1*3 + 1*4 = 28
이 된다. 이러한 형택이의 곱셈 결과를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. 주어지는 두 수는 모두 10,000자리를 넘지 않는 음이 아닌 정수이다. 수가 0인 경우에는 0만 주어지며, 그 외의 경우 수는 0으로 시작하지 않는다.

출력
첫째 줄에 형택이의 곱셈 결과를 출력한다.'''

import sys
sys.stdin = open("input.txt", "r")

A, B = list(map(str,input().split()))
A = [int(a) for a in A]
B = [int(b) for b in B]
print(sum(A)*sum(B))

'''
# result = 0
# A, B = list(map(list,input().split()))
# for a in A:
#     for b in B:
#         result += int(a)*int(b)
# print(result)
'''
'''
121 * 34

length = len(str(121)
100 = 10**length
121/100 = 1.21

a1 = divmod(121, 100)
> (1, 21)
a2 = divmod(a1[1], 100/10)
> (2, 1)
a3 = a2[1]
'''

"""
import sys
sys.stdin = open("input.txt", "r")

result = 0
list_a = []
list_b = []

A, B = list(map(int,input().split()))

while True:
    # A와 B 값을 반복에서 10으로 나눈 나머지를 빈 리스트에 더하기
    # divmod(x,y) (x//y, x%y)
    a = divmod(A, 10)
    b = divmod(B, 10)

    # 나머지값[1]을 리스트에 추가
    list_a.append(a[1])
    list_b.append(b[1])

    # 몫[0]을 나눌 대상(A, B)으로 변환
    A = a[0]
    B = b[0]

    # 나눌 대상이 모두 0이 될때까지 반복
    if a[0] == 0 and b[0] == 0:
        break
# 리스트를 순회하면서 각각의 값을 곱한다.
for list_a_num in list_a:
    for list_b_num in list_b:
        # 곱셈한 값은 result변수에 더해 결과를 출력
        result += list_a_num*list_b_num
print(result)

'''
121 * 34

length = len(str(121)
100 = 10**length
121/100 = 1.21

a1 = divmod(121, 100)
> (1, 21)
a2 = divmod(a1[1], 100/10)
> (2, 1)
a3 = a2[1]
'''
"""