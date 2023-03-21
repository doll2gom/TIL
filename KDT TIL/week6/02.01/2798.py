# BOJ 2798 블랙잭
'''
문제
M을 넘지 않으면서 M과 최대한 가까운 3장의 합

입력
첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 
둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.

출력
첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.'''

import sys
sys.stdin = open("input.txt","r")

N, M = map(int, input().split())
cards = list(map(int, input().split()))

def blackjack(N,M,cards):
    max_total = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                total = cards[i] + cards[j] + cards[k]

                if max_total < total <= M:
                    max_total = total
                
                if total == M:
                    return total
    return max_total
print(blackjack(N, M, cards))