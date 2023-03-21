''' 10250번 ACM 호텔
입력
프로그램은 표준 입력에서 입력 데이터를 받는다. 프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다. 각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다(1 ≤ H, W ≤ 99, 1 ≤ N ≤ H * W). 

출력
프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행을 출력하는데, 내용은 N 번째 손님에게 배정되어야 하는 방 번호를 출력한다.'''
"""2
6 12 10
30 50 72"""

import sys
# sys.stdin = open("input.txt", "r")
T = int(sys.stdin.readline())
for t in range(T):
    H, W ,N = map(int,sys.stdin.readline().split())
    room = divmod(N,H)
    y = room[0]+1
    x = room[1]
    if y < 10:
        x *= 100
    print(x+y)