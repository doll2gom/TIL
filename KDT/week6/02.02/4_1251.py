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
import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint
import heapq

lst = []
word = str(input())
length = len(word)
# length_graph = [ [0] * length for _ in range(length)]
# pprint(length_graph)
for _ in word:
    heapq.heappush(lst, ord(_))
    print(ord(_))
print(lst)
for w in lst:
    print(chr(w), end = ' ')
print()
print()

cnt = 0
# 문자열을 3 덩어리로 나눌 수 있는 모든 경우의 수 인덱스를 찾는다.
for i in range(0,7-2):
    for j in range(i+1,7-1):
        for k in range(j+1,7):
            print(cnt, word[i], word[j], word[k])
            cnt += 1
            print(word[i::-1] , word[i+1:k-1:-1] , word[j+1::])
            print()
            print()

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
"""mobitel"""