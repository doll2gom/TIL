T = int(input())
for test_case in range(1, T + 1):
    t = list(map(int,input().split()))
    b = 0
    for n in t:
        numbers = []
        if n%2 == 1:
            numbers.append(n)
            for a in numbers:
                b += a
    print(f'#{test_case} {b}')