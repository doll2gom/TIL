''' 7568번 덩치
문제
몸무게가 x kg이고 키가 y cm라면 이 사람의 덩치는 (x, y)로 표시된다. 
두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p 그리고 y > q 이라면 A의 덩치가 B의 덩치보다 "더 크다"

N명의 집단에서 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다. 
만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다. 이렇게 등수를 결정하면 같은 덩치 등수를 가진 사람은 여러 명도 가능하다. 아래는 5명으로 이루어진 집단에서 각 사람의 덩치와 그 등수가 표시된 표이다.

이름 (몸무게, 키) 덩치 등수
A	(55, 185)	2
B	(58, 183)	2
C	(88, 186)	1
D	(60, 175)	2
E	(46, 155)	5
위 경우에 3등과 4등은 존재하지 않는다. 

입력
첫 줄에는 전체 사람의 수 N이 주어진다. 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.

출력
여러분은 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력해야 한다. 단, 각 덩치 등수는 공백문자로 분리되어야 한다.

제한
2 ≤ N ≤ 50
10 ≤ x, y ≤ 200'''

import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

# 인접리스트 
# 리스트 안에 N개의 리스트가 필요
# def pprint(arr):
# 	for row in arr:
# 		print(*row)
from pprint import pprint

N = int(input())
people = []
for n in range(N):
	x, y = list(map(int, input().split()))
	people.append((x,y))

TF = []
cnt = 0
for i in range(N):
	for j in range(N):
		# if info[0] > lst_[i][0] and info[1] > lst_[i][1]:
		if people[i][0] < people[j][0] and people[i][1] < people[j][1]:	# 몸무게 키 비교
				cnt += 1	# 나보다 덩치큰 사람 카운트
	TF.append(cnt+1)	# N명의 집단에서 등수는 자신보다 더 "큰 덩치"의 사람의 수
	cnt = 0
print(*TF,end=' ')