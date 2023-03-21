''' 2167번 2차원 배열의 합
문제
2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 
배열의 (i, j) 위치는 i행 j열을 나타낸다.

입력
첫째 줄(행,가로)에 배열의 크기 N, M
N개의 줄(행,가로)에는 M(열,세로)배열
다음 줄에는 합을 구할 부분의 개수 K
다음 K개의 줄에는 네 개의 정수로 i, j, x, y

출력
K개의 줄에 순서대로 배열의 합을 출력
배열의 합은 2**31-1보다 작거나 같다.'''

import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint
N, M = sys.stdin.readline().split()
matrix = [ list(map(int,sys.stdin.readline().split())) for n in range(int(N))]
pprint(matrix)
K = int(sys.stdin.readline())
for k in range(K):
    a, b, c, d = list(map(int,sys.stdin.readline().split()))
    print(a, b, c, d)
    if a == c and b == d:
        print(matrix[a][b])
    else:
        print( sum(matrix[a-1][b-1:]) + sum(matrix[c-1][:d-1]))

# 164ms
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
d = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        d[i][j] = li[i-1][j-1] + d[i][j-1] + d[i-1][j] - d[i-1][j-1]
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(d[x][y] - d[x][j-1] - d[i-1][y] + d[i-1][j-1])

"""
i(입력)
    0   1   2
0   1   2   4
1   8   16  32

    1   2   3
1   1   2   4
2   8   16  32

d(누적합) 기록
    0   1   2   3
0   0   0   0   0
1   0   1   3   7
2   0   9   27  63

예를 들어 d[2][2] 를 구하기 위해서는 i[0][0] + i[0][1] + i[1][0] + i[1][1]해야 함
d로 묶어서 써보면
d[1][2](i[0][0] + i[0][1]) + i[1][0] + i[1][1]
=> d[2][1](i[0][0] + i[1][0]) - i[0][0] + d[1][2](i[0][0] + i[0][1]) + i[1][1]
=> d[2][1] + d[1][2] + i[1][1] - i[0][0]
for문을 돌릴때 범위를 (1, N+1), (1, M+1)로 지정했으므로
d[i]d[j] = i[i-1][j-1] + d[i][j-1] + d[i-1][j] - d[i-1][j-1]를 누적합배열에 저장
그리고 처음부터가 아닌 중간부터 어느 범위까지의 누적합을 구할때는 범위에 들어오지 않는 값을 뺴줘야함
예시 누적합 테이블
    1   2   3       4
1   
2           시작    
3                  끝
i, j, x, y가 2 3 3 4인 경우 전체 누적합에서 테이블[3][4] 범위에 들어오지 않는 값을 뺴줘야 함
테이블[3][2], 테이블[1][4] 빼고 테이블[1][2]는 두 번 빼지므로 한 번 더해줌
=> 결과값 = d[x][y] - d[x][j-1] - d[i-1][y] + d[i-1][j-1]
d[x][y] - d[x][y-2] - d[x-2][y] + d[x-2][y-2]: 틀림=>주어진 값이 바뀌면 빼는 숫자가 바뀌기 때문
=> 불변값들만 사용
"""
# 88ms
from itertools import accumulate
import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))
d = [None] * (N +1)
d[0] = [0 for _ in range(M+1)]
for i in range(1, N+1):
    d[i] = accumulate(list(map(int, input().split())), initial=0)
    d[i] = [x+y for x, y in zip(d[i-1], d[i])]
K = int(input().rstrip())
res = [None] * K
for n in range(K):
    i, j, x, y = list(map(int, input().split()))
    res[n] = d[x][y] - d[x][j-1] - d[i-1][y] + d[i-1][j-1]
print(*res, sep = '\n')