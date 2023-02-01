'''문제
m행 n열로 이루어진 그리드가 주어진다. 
박스가 움직인 거리는 바닥에 쌓이기 전 까지 이동한 칸의 개수이다.
m = 세로
n = 가로

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
각 테스트 케이스의 첫째 줄에는 m과 n이 주어진다. (1 ≤ m, n ≤ 100) 
박스가 들어있는 칸은 1, 다른 칸은 0
각 정수 사이에는 공백이 하나 주어진다.

출력
모든 박스가 이동한 거리를 출력한다.'''

import sys
sys.stdin = open("input.txt", "r")

test_case = int(input())
for _ in range(1, test_case+1):
    # m세로, n가로 길이 입력받음
    m, n = map(int, input().split())

    # 2차원 리스트로 그리드를 입력받음
    grid = [ list(map(int, input().split())) for _ in range(m)]

    # 가로세로 길이가 같은 0으로 체워진 2차원 리스트 준비
    transposed_grid = [[0]* m for _ in range(n)]

    # # 시계 반대방향으로 90도 회전? 전치?
    for i in range(n):
        for j in range(m):
            transposed_grid[i][j] = grid[j][i]

    move = 0
    for i in range(n):
        for j in range(m,-1,-1):
            print(j)
            if transposed_grid[i][j] == 0:
                line = transposed_grid[i]
                if 1 not in line[:j]:
                    move += line.count(0)
                    line = transposed_grid[i]
                    del line[:j]
            # elif 1 not in transposed_grid[i]:
            #     if 
            #         line = transposed_grid[i]
            #         move += line.count(0)
                pass
    print(move)
    move = 0



'''
1 0 0 0
0 0 1 0
1 0 0 1
0 1 0 0
1 0 1 0
>>
1 0 1 0 1
0 0 0 1 0
1 0 0 1 0
0 0 1 0 0
'''

'''
<빈공간 조건 이동 조건 두 가지>
① 박스 아래에 박스가 X
현재 박스 grid[y][x]
다음 위치(grid[y+1][x] ! = 1)

② 박스 아래가 범위를 벗어나면 X
현재 박스 grid[y][x]
다음 위치 (y+1 < m)
'''

grid = [
[0, 0],
[0, 1],
[1, 0],
[0, 0],
[0, 1],
]

m = 5 # 세로(행)
n = 2 # 가로(열)

# 탐색 방향은???????
# 행 우선 -> y축을 먼저 움직여야하는지 
# 열 우선 -> x축을 먼저 움직여야하는지

# 박스 이동
move_dis = 0
for x in range(n):
    for y in reversed(range (m)) :
        # print (y, x, grid[y][x])

        # 박스를 이동시키기위해
        # 박스를 찾자!  
        if grid[y][x] == 1:
            # 조건이 만족하면
            # 박스를 이동
            while True:
                # 조건을 작성할 때 최우선 순위는 범위를 체크하는 것

                # 조건 1를 만족하는지?
                # 다음 위치가 범위를 벗어나면 박스 이동 X
                if y+1 == m:
                    break

                # 조건 2을 만족하는지?
                # 다음 위치에 박스가 있을 때 박스 이동 X
                if grid[y+1][x] == 1:
                    break
                # 현재 위치는 비우고, 
                grid[y][x]= 0 
                # 다음 위치로 박스가 이동
                grid [y+1][x] = 1
                move_dis += 1

# from pprint import print
def pprint(arr):
    for a in arr:
        print(*a)
        
pprint(grid)
print(move_dis)