''' 2846번 오르막길
문제
오르막길, 내리막길, 평지, 가장 큰 오르막길의 크기?
높이는 길이가 N인 수열로 나타낼 수 있다. 여기서 오르막길은 적어도 2개의 수로 이루어진 높이가 증가하는 부분 수열이다. 오르막길의 크기는 부분 수열의 첫 번째 숫자와 마지막 숫자의 차이이다.

입력
측정한 수이자 수열의 크기인 N(1 ≤ N ≤ 1000)이 주어진다. 
둘째 줄에는 N개의 양의 정수 Pi(1 ≤ Pi ≤ 1000)가 측정한 높이이다.

출력
첫째 줄에 가장 큰 오르막길의 크기를 출력한다. 오르막길이 없는 경우 0을 출력한다.'''

import sys
sys.stdin = open("input.txt", "r")

M = int(input()) # M과 M번 측정한 높이들을 입력받는다.
way = list(map(int, input().split()))

lst = [] # 리스트를 준비해 모든 오르막길의 높이를 모은다.
cnt = 0  # 이동한 거리를 카운트하여 오르막길의 시작과 끝의 인덱스를 특정
for h in range(0,M): # 측정한 횟수만큼 반복하며 알아본다.
    if way[h] < way[(h+1)%M]:      # 현위치 vs 앞위치 오르막의 끝인지 확인
        cnt += 1 # 이동거리를 카운트   #(h+1)%M는 인덱스 범위를 넘어서지 않기 위한 장치이다.
    elif way[h] >= way[(h+1)%M]:   # 오르막의 끝이라면
        high = way[h] - way[h-cnt] # 현위치에서 오르막이 시작한 지점의 높이를 빼기
        lst.append(high)           # 구한 오르막의 높이를 리스트에 모은다.
        cnt = 0  # 오르막 이동거리 0으로 초기화
print(max(lst))  # 오르막 높이 모음에서 최댓값 출력


'''
5
1 2 1 4 6
>> 5

8
12 20 1 3 4 4 11 1
>> 8

6
10 8 8 6 4 3
>> 0'''
