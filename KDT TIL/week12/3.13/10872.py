''' 10872번 팩토리얼 성공
문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

출력
첫째 줄에 N!을 출력한다.'''
import sys
N = int(sys.stdin.readline())
# 2! = 2 * 1
# 3! = 3 * 2 * 1 = 3 * 2!
# 4! = 4 * 3 * 2 * 1 = 4 * 3!
# N! = N * (N-1)!

def f(n):
    N = n
    if n == 0:
        return 1
    else:
        return n * f(n-1)
print(f(N))
    # for i in range(1, N+1):
