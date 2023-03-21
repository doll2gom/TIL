''' 1547번 공
문제
맨 왼쪽부터 1번, 2번 3번
먼저 1번 아래에 공 하나 위치를 바꿔도 공의 위치는 맨 처음 1번 위치와 같다.
위치를 M번 바꾼 이후에 공이 들어있는 컵의 번호를 구하는 프로그램을 작성하시오.

입력
첫째 줄메 위치를 바꾼 횟수 M은 50보다 작거나 같은 자연수
둘째 줄부터 M개의 줄에 X와 Y가 주어지며, X번 컵과 Y번 컵의 위치를 서로 바꾸는 것을 의미

출력
첫째 줄에 공이 들어있는 컵의 번호를 출력한다. 공이 사라져서 컵 밑에 없는 경우에는 -1을 출력한다.'''

import sys
sys.stdin = open("input.txt", "r")

ball = [1, 2, 3]   # 초기 상태를 리스트로 준비
M = int(input())
for _ in range(M):             # M회 반복하며, x와 y를 입력받음
    x, y = map(int, input().split()) # 1, 2         
    index_x = ball.index(x)          # index_x = 0  # 해당 번호의 인덱스를 구함
    index_y = ball.index(y)          # index_y = 1
    ball[index_x] = y                # 2 2 3        # 인덱스에 교차하여 번호 수정
    ball[index_y] = x                # 2 1 3
print(ball[0])

'''
4
3 1
2 3
3 1
3 2'''