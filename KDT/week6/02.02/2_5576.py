''' 5576번 콘테스트 
문제
10 명씩이 콘테스트에 참여, 높은 3 명의 점수를 합산

입력
20 행으로 구성, 1~10 행 W 점수, 11~20 행 K 점수

출력
W ,K 점수를 순서대로 공백으로 구분하여 출력'''
# 기존에 제출한 풀이 
'''
w = []
k = []
cnt = 0
cnt2 = 0
for i in range(0,10):
    W = int(input())
    w.append(W)
for i in range(0,10):
    K = int(input())
    k.append(K)
for l in range(0,3):
    mw = max(w)
    mk = max(k)
    cnt += mw
    cnt2 += mk
    w.remove(mw)
    k.remove(mk)
print(cnt, cnt2)
'''

import sys
sys.stdin = open("input.txt", "r")

# 코드 길이는 짧아졌지만 시간은 좀 더 걸림 
# 36ms > 40ms
W = [ int(input()) for i in range(10)]
K = [ int(input()) for i in range(10)]
print(sum(sorted(W)[7:11]),sum(sorted(K)[7:11]))