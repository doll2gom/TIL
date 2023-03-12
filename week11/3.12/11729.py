''' 11729번 하노이 탑 이동 순서
문제
세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다.

한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

입력
첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.

출력
첫째 줄에 옮긴 횟수 K를 출력한다.
두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.'''

import sys
def hanoi(N, a, b, c):
    if N == 1:
        print(a, b)
    else:
        hanoi(N -1, a, c, b)
        print(a, b)
        hanoi(N -1, c, b, a)

N = int(sys.stdin.readline())
print((2 ** N) - 1)
hanoi(N, "1", "3", "2")


# ===========================
cnt = 0
def 하노이탑(원판개수, 시작, 목표, 보조):
    global cnt
    if 원판개수 == 1:
        print(시작, "->", 목표)
        cnt += 1
    else:
        하노이탑(원판개수 - 1, 시작, 보조, 목표)
        print(시작, "->", 목표)
        cnt += 1
        하노이탑(원판개수 - 1, 목표, 보조, 시작)
원판개수 = int(sys.stdin.readline())
하노이탑(원판개수, "A", "B", "C")
print(cnt)
