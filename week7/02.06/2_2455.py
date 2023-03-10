''' 2455번 지능형 기차
문제
역에서 기차에 탈 때, 내릴 사람이 모두 내린 후에 기차에 탄다고 가정한다.
기차는 역 번호 순서대로 운행한다.
출발역에서 내린 사람 수와 종착역에서 탄 사람 수는 0이다.
각 역에서 현재 기차에 있는 사람보다 더 많은 사람이 내리는 경우는 없다.
기차의 정원은 최대 10,000명이고, 정원을 초과하여 타는 경우는 없다.
4개의 역에 대해 기차에서 내린 사람 수와 탄 사람 수가 주어졌을 때, 기차에 사람이 가장 많을 때의 사람 수를 계산
입력
각 역에서 내린 사람 수와 탄 사람 수가 빈칸을 사이에 두고 첫째 줄부터 넷째 줄까지 역 순서대로 한 줄에 하나씩 주어진다. 
출력
첫째 줄에 최대 사람 수를 출력한다.  '''

import sys
sys.stdin = open("input.txt", "r")

max_train = 0	# 최대인원
people_cnt = 0	# 기차에 있는 인원

for station in range(4):	# 기차역은 4개로 정해져 있다. 
	on, off = map(int, input().split())	# 내리는 사람과 타는 사람 수를 입력받음
	people_cnt -= on	# 문제에서 먼저 다 내리고 그 다음 올라탄다고 정해져 있다. 
	people_cnt += off

	if people_cnt > max_train: # 최대인원보다 기차에 있는 인원이 많으면 갱신
		max_train = people_cnt
print(max_train)