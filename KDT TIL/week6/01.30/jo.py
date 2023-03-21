'''
2행 3열 리스트 두 개에 각각의 값을 입력 받은 후 두 배열의 같은 위치끼리 곱하여 새로운 리스트에
저장한 후 출력하는 프로그램을 작성하시오. 
'''
import sys
sys.stdin = open("input.txt", "r")
A_list = [ list(map(int,input().split())) for _ in range(2)]
B_list = [ list(map(int,input().split())) for _ in range(2)]
c = []
for n1 in range(2):
    for n2 in range(3):
        c.append(A_list[n1][n2]*B_list[n1][n2])
    print(*c)
    c.clear()