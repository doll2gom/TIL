''' 4963번 섬의 개수 
문제
한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 
입력
각 테스트 케이스
1. 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
2. h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.'''

import sys
sys.stdin = open("input.txt", "r")
def pprint(arr):
    for row in arr:
        print(*row)

w, h = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(h+1)]
graph = [ [] for _ in range(h+1)] 
for y in range(h):
    for x in range(w):
        if matrix[y][x] == 1:
            graph[y].append((y,x))
print(sorted(graph))


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
# print(dfs(0))