import sys
sys.stdin = open("input.txt", "r")
import pprint

# # 1-1
# matrix = []
# for i in range(8):
#     txt = str(input())
#     matrix.append(list(txt))
# pprint.pprint(matrix)

# 1-2
cnt = 0
matrix2 = [list(input()) for _ in range(8)]
# 행대로 반복
for m1 in range(8):
    for m2 in range(8):
        if (m1+m2)%2 == 0:
            if matrix2[m1][m2] == 'F':
                cnt += 1
print(cnt)

# 2. 3X3
# line = '1, 2, 3'
# [1, 2, 3]
# input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix3 = [ list(map(int,input().split())) for i in range(8)]
# pprint.pprint(matrix3, sep=' ')