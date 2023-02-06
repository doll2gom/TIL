''' 2606번 바이러스
문제
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 컴퓨터의 수가 주어진다. 
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

출력
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.'''
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

dot = int(input())
line = int(input())
graph = [ [ ] for _ in range(dot+1)]
for l in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)

visited = [False] * dot # 방문 처리 리스트 만들기
print(visited)
def dfs(start):
    cnt = 0
    stack = [start] # 돌아갈 곳을 기록
    visited[start]= True # 시작 정점 방문 처리
    while stack: # 스택이 빌 때까지 (돌아갈 곳이 없을때까지) 반복
        cur = stack.pop() # 현재 방문 정점(후입선출)
        for adj in graph[cur]: # 인접한 모든 정점에 대해
            if not visited[adj]: # 아직 방문하지 않았다면(False)
                visited[adj] = True # 방문 처리(True 변경)
                stack.append (adj) # 스택에 넣기
                cnt += 1

    return cnt
print(dfs(1))