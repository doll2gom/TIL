''' 4963번 섬의 개수 
문제
한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 
입력
각 테스트 케이스
1. 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
2. h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
입력의 마지막 줄에는 0이 두 개 주어진다.

출력 섬의 개수를 출력한다.'''
"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7"""
# graph = [
#     [],
#     [2, 5],
#     [1, 3, 5],
#     [2],
#     [7],
#     [1, 2, 6],
#     [5],
#     [4]
# ]

# 컴퓨터 바이러스 문제처럼 먼저 데이터를 만들 수 없을까?


import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint

# 가로 세로 길이 입력받음
w, h = map(int, input().split())
# 섬 지도 입력받음
matrix = [ list(map(int, input().split())) for _ in range(h)]
# pprint(matrix)


# 방문 체크 리스트
visited = [ [ True ] * w for _ in range(h)]  
# pprint(visited)

# 땅인지 아닌지 컴퓨터 바이러스처럼 좌표값을 튜블로 입력받음
land = {}
# pprint(land)

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
# 지도를 돌면서 현위치에 1이 있으면 인접한 노드의 최표값을 찾는다.(8방향) 
# 높이와 넓이가 다를 수 있기 때문에 h,w를 따로 반복문으로 돌린다.
for x in range(h):
    for y in range(w):
        # x는 세로높이 y는 가로넓이
        if matrix[x][y] == 1:
            m_xy = f'({x},{y})'
            land[m_xy] = []

            # 방문 리스트에 체크
            # visited[x][y] = False
            # pprint(land)
            # pprint(visited)

            # matrix 현위치 주변(8방향)에 1이 있는지 확인
            # 8방향 델타를 확인하기 때문에 0~7까지 리스트를 돌면서 확인하는 것
            for i in range(8):  # 지도에서 현위치인  matrix[x][y]를 기준으로
                nx = x + dx[i]  # 주변 노드 matrix[nx][ny] 8개를 확인하기 위함이다. 
                ny = y + dy[i]  # nx와 ny는 델타값을 확인하기 때문에 8번 변한다.


                # 방금 생성한 nx,ny 좌표를 x,y로 설정하기 전에
                # matrix 지도를 벗어나지는 않는지 확인한다.
                # x,y가 0,0이면 좌측 상단이기 때문에 상관없다. 
                # 하지만, 지도 밖으로 범위를 벗어나면 안 된다. 
                if 0 <= nx < h and 0 <= ny < w:
                    x = nx
                    y = ny
                    # print((x,y))
                    # print(m_xy)
                    a = list(land[m_xy])
                    a.append((x,y))
                    land[m_xy] = a
    pprint(land)
    print('--')


# def dfs(start):
#     cnt = 0
#     stack = [start] # 돌아갈 곳을 기록
#     visited[start]= True # 시작 정점 방문 처리
#     while stack: # 스택이 빌 때까지 (돌아갈 곳이 없을때까지) 반복
#         cur = stack.pop() # 현재 방문 정점(후입선출)
#         for adj in graph[cur]: # 인접한 모든 정점에 대해
#             if not visited[adj]: # 아직 방문하지 않았다면(False)
#                 visited[adj] = True # 방문 처리(True 변경)
#                 stack.append (adj) # 스택에 넣기
#                 cnt += 1
# pprint(graph)


'''
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0'''

'''
# while True:
#     w, h = map(int, input().split())
#     if w == h == 0:
#         break
#     else:
#         matrix = [ list(map(int, input().split())) for _ in range(h)]
#         graph = [ [] for _ in range(h)] 
#         visited = [ [False]*w for _ in range(h)]   # 방문기록지
#         def dfs(start):
#             stack = [start]
#             visited[start] = True

#             while stack:    
#                 cur = stack.pop()  
#                 for adj in graph[cur]:
#                     print(adj)
#                     if not visited[adj]: 
#                         visited[adj] = True 
#                         stack.append (adj) 
#             return visited.count(True)

#         print(dfs(0))
#         pprint(visited)
#     pprint(graph)

        # if graph[0] == []:
        #     print(0)
        # else:
        #     print(visited)

# graph = [
# [1, 2],
# [0, 3, 4],
# [0, 4, 5],
# [1],
# [1, 2, 6],
# [2],
# [4]
# ]

# visited = [False] * 49 # 방문 처리 리스트 만들기
# def dfs (start):
#     stack = [start] # 돌아갈 곳을 기록
#     visited[start]= True # 시작 정점 방문 처리
#     # print(start, type(stack),stack, visited[start])
#     # print(visited)
#     while stack: # 스택이 빌 때까지 (돌아갈 곳이 없을때까지) 반복
#         cur = stack.pop() # 현재 방문 정점(후입선출)
#         # print(start, stack,'///', cur)

#         for adj in graph[cur]: # 인접한 모든 정점에 대해
#             if not visited[adj]: # 아직 방문하지 않았다면
#                 visited[adj] = True # 방문 처리
#                 stack.append (adj) # 스택에 넣기
# print(dfs(0))'''