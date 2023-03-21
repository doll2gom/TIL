''' 1546번 평균
자기 점수 중에 최댓값을 M이라고 한다. 모든 점수를 점수/M*100으로 고쳤다.

예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.

세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 시험 본 과목의 개수 N이 주어진다.
둘째 줄에 세준이의 현재 성적이 주어진다.
출력
첫째 줄에 새로운 평균을 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.'''

import sys
sys.stdin = open("input.txt", "r")

lst = []
N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
for score in scores:
    lst.append(score/M*100)
print(sum(lst)/len(scores))