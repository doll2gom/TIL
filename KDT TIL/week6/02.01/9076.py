''' 9076번 점수 집계
문제
이전에는 5명의 최고점과 최저점을 하나씩 제외한 점수의 합을 총점으로 
최고점과 최저점을 뺀 나머지 3명 점수의 최고점과 최저점의 차이가 4점 이상 나게 되면 다시,
총점을 계산하거나, 점수 조정을 거쳐서 다시 점수를 매기려고 하는 경우에 총점 대신 KIN(Keep In Negotiation)을 출력

입력
입력의 첫 줄에는 테스트 케이스의 개수 T
한 줄에 다섯 개의 정수 Ni(1 ≤ Ni ≤ 10, i = 1, 2, ..., 5)가 하나의 공백을 사이에 두고 주어진다.

출력
각 테스트 케이스에 대해서 총점을 한 줄씩 출력한다. 
만일 점수 조정을 거쳐서 다시 점수를 매기려고 하는 경우에는 총점 대신 KIN을 출력한다.'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# T만큼 리스트 입력받으면서 바로 순서대로 정렬sorted
test_case =[ sorted(list(map(int, input().split()))) for _ in range(T)]
# 각 리스트마다 
for t in test_case:
    # 인덱스[3]-[1]의 값이 4이상이면 KIN출력 
    if t[3] - t[1] >= 4:
        print('KIN')
    else:
        print(sum(t[1:4]))