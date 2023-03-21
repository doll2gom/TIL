''' 2908번 상수
문제
상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
입력
첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다.
출력
첫째 줄에 상수의 대답을 출력한다.'''

import sys
sys.stdin = open("input.txt", "r")

N = int(input())
for n in range(N):
    a, b= map(int, input().split())
    l = []
    for n in range(3):
        ans = a//100
        l.append(ans)
        a = a%10
        l.append(a)
        a = a%1
        l.append(a)
        print(l)