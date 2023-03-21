''' 1251번 단어 나누기
문제
알파벳 소문자로 이루어진 단어
단어를 길이가 1 이상인 세 개의 더 작은 단어로 나누는
나눈 세 개의 작은 단어들을 앞뒤를 뒤집고, 이를 다시 원래의 순서대로 합친다.

단어 : arrested
세 단어로 나누기 : ar / rest / ed
각각 뒤집기 : ra / tser / de
합치기 : ratserde

단어가 주어지면, 이렇게 만들 수 있는 단어 중에서 사전순으로 가장 앞서는 단어를 출력하는 프로그램을 작성하시오.
입력
첫째 줄에 영어 소문자로 된 단어가 주어진다. 길이는 3 이상 50 이하이다.

출력
첫째 줄에 구하고자 하는 단어를 출력하면 된다.'''
'''
<0203 오전 강사님 풀이>
# 문자열을 두 번 나누는 모든 경우의 인덱스를 구한다.

인덱스 0 1 2 3 4 5 6 7
문자열[a r r e s t e d]

N = 8

i : 처음 잘라내는 지점
i >> 최소길이 min = 1     # 인덱스[1] 앞에서 자름
     최대길이 max = N-2   # 인덱스[N-1] 앞에서 자름
range(1, N-1)
: 1 2 3 4 5 6

j : 두번째 잘라내는 지점
j >> 최소길이 min = i+1   # 인덱스[i+1] 앞에서 자름
     최대길이 max = N-1   # 인덱스[N] 앞에서 자름
range(1, N-1)
range(1, N-1)
: 1 2 3 4 5 6
'''

"""mobitel"""

import sys
sys.stdin = open("input.txt", "r")

import heapq
lst = []
word = str(input())        # mobitel
N = len(word)

# 나누는 위치의 인덱스 구하기 (총 2번 나눔)
# 첫 번째 경우를 생각했을 때, i는 인덱스[1] 앞(=인덱스[0]뒤) ~ 맨 뒷자리의 문자 바로 앞에서 나눔
for i in range(1,N-1):     # i = 1   
    for j in range(i+1,N): # j = range(2,N)
        w1 = word[0:i]     # w1 = m     
        w2 = word[i:j]     # w2 = o
        w3 = word[j:N]     # w3 = bitel
        # 구한 인덱스 위치로 두번 나누어 만는 3개의 문자열 덩어리
        # 각각 인덱스로 뒤집은 뒤, heapq를 사용해 리스트에 정렬하여 넣는다.
        heapq.heappush(lst, f'{w1[::-1]+ w2[::-1]+ w3[::-1]}')

print(lst[0]) # heapq를 사용해 순서를 정렬해 놨기 때문에 맨 처음 문자열을 출력
'''
from pprint import pprint
import heapq
for _ in word:
    heapq.heappush(lst, ord(_))
    print(ord(_))
print(lst)
for w in lst:
    print(chr(w), end = ' ')
print()
print()
'''
'''
# 0 1
# 0 2
# 1 3
# 1 4
# 2 4
# 2 5
# 4 6
# 인접 행렬
# 7 * 7
# 정점간의 관계를 표현하고 있는 행렬
# 정접의 개수인 N에 의해 크기가 정해짐
N = 7
graph = [ [0] * N for _ in range (N)]

pprint(graph)
'''
