import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    i = 1
    numbers = set()
    while True:
        for n in str(N):
            if n not in numbers:
                numbers.add(int(n))
        if len(numbers) == 10:
            break
        N //= i
        i += 1
        N *= i
    print(f"#{test_case} {N}")