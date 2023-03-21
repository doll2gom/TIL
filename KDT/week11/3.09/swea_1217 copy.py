'''다음과 같이 두 개의 숫자 N, M이 주어질 때, N의 M 거듭제곱 값을 구하는 프로그램을 재귀호출을 이용하여 구현해 보아라.

2 5 = 2 X 2 X 2 X 2 X 2 = 32
3 6 = 3 X 3 X 3 X 3 X 3 X 3 = 729

[제약 사항]
총 10개의 테스트 케이스가 주어진다.
결과 값은 Integer 범위를 넘어가지 않는다.
[입력]
각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 두 개의 숫자가 주어진다.
[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.'''

import sys
sys.stdin = open("input.txt", "r")

# 반복문으로 구현
def loop(n, m):
    output = 1
    for _ in range(1, m+1):
        output *= n
    return output

while True:
    try:
        t = int(input())
        n, m = map(int, input().split())
        print(f"#{t} {loop(n, m)}")
    except:
        break

# 재귀함수로 구현
# 수열의 점화식
# 이웃한 항의 관계를 통해 수열을 나타내는 것

def rcrs(n, m): # 3 2
    # n * 1 = n
    if m == 1: 
        return n 
    # n *= n
    elif m >= 2:    # m이 2 이상의 수일 때 
        return n * rcrs(n, m-1)

while True:
    try:
        t = int(input())
        n, m = map(int, input().split())
        print(f"#{t} {rcrs(n, m)}")
    except:
        break
