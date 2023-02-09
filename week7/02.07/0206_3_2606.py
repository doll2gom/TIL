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
'''
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
print(dfs(1))'''
'''
<DFS의 기본 형태>

1. 시작점 (1)문제에서 주어지는 경우 (2) 탐색을 해서 찾는 경우 >> 바이러스 문제에서는 1번으로 시작점이 지정되어 있다. 
2. 스택(방문한 정점을 넣을)
    방문여부 확인 변수
3. 스택에 시작점 push(append)
4. 무한반복 -> 스택의 길이가 0이 아니면
5-1 스택에서 값 꺼내기, 현재 정점
5-2 인접 정점 확인 
내가 푸는 문제가 1차원인지 2차원인지 확인 후 방향을 사용
(델타변수를 사용해서 상하좌우 or 8방향 모두 탐색 가능)
5-3 한번도 방문하지 않은 인접 정점인지 확인
5-3-1 (방문한 적 없다면, 방문하기 위해) 스택에 인접 정점 push(append)
5-3-2 방문했다면, 방문표시한다.

문제의 요구는 저마다 다양하다.
- DFS를 총 몇번 실행하는지 
- DFS를 실행했을 때 방문한 순서의 노드의 번호작성
- 길 찾기
- 미로를 주고 나갈 수 있는지 여부
- 특정 지점에 도착힐 수 있는지 여부

'''

# 1. 1번으로 시작점이 지정되어 있다. 
# 4. 무한반복이 몇번 일어나는지 확인하라

import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint


# 정점의 수:
N = int(input())

# 간선의 수
M = int(input())

# 그래프 표현 방법 1
# 인접리스트
# 리스트의 수는 노드의 수(N개) 만큼 있어야하는데, 개발자에게는 0부터 시작함 
# 방법 1 1부터 11까지 = 10개
# 방법 2 0부터 11까지 = 11개
# 방법2를 선호하자 그냥 빈 리스트를 하나 더 만들어 버리자
# N+1 만큼 리스트를 가진 리스트
graph = []
for _ in range(N+1):
    graph.append([])

# print(graph)

# 정점의 쌍 입력(간선만큼)
for _ in range(M):
    node1, node2 = list(map(int, input().split()))

    # 양방향 그래프
    # node1의 인접리스트에 node2를 추가
    graph[node1].append(node2)

    # node2의 인접리스트에 node1를 추가
    graph[node2].append(node1)

### 1
# 시작점
start = 1

### 2
# 스택
stack = []
# 방문여부를 확인할 변수
# visit = [False] * (N+1)

# 꼬아보자면 중복을 확인할 때 사용하는 자료구조는?
# 바로 set데이터 타입을 활용하여 방문 여부를 확인 가능
# set의 탐색은 시간복잡도 또한 O(1)로 훨씬 가벼워진다
visit = set()

### 3
stack.append[start]

### 4
# 스택 리스트 안에 아무것도 없을 때까지
# = 스택 리스트의 길이가 0이 될 때까지
while len(stack) != 0:

    ### 5-1
    # 스택에 들어있는 값 순서대로 방문
    # 방문한 값은 현재값으로 취하면서 동시에 스택에서 삭제
    current_node = stack.pop()

    ### 5-2 
    # 양방향을 표현한 graph에서 인접 정점을 확인 
    
    adj_graph = graph()

print(graph)
