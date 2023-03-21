''' 24416번 알고리즘 수업 - 피보나치 수 1
문제
아래 의사 코드를 이용하여 n의 피보나치 수를 구할 경우 코드1 코드2 실행 횟수를 출력하자.

피보나치 수 재귀호출 의사 코드

fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
    else return (fib(n - 1) + fib(n - 2));
}
피보나치 수 동적 프로그래밍 의사 코드는 다음과 같다.

fibonacci(n) {
    f[1] <- f[2] <- 1;
    for i <- 3 to n
        f[i] <- f[i - 1] + f[i - 2];  # 코드2
    return f[n];
}
입력
첫째 줄에 n(5 ≤ n ≤ 40)이 주어진다.

출력
코드1 코드2 실행 횟수를 한 줄에 출력한다.'''

import sys
n = int(sys.stdin.readline())
cnt1 = 0
cnt2 = 0
f = [ i for i in range(0, n+1)]

def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def dp(n):
    global cnt2
    f[1] == f[2] == 1
    for i in range(3, n+1):
        cnt2 += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

fib(n)
dp(n)
print(cnt1, cnt2)
