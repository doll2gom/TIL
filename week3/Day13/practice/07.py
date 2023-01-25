T, N = list(map(int,input().split())) # 테스트 케이스 수
print(T, N)
for t in range(1, T+1):
    for s in range(1, N+1):
        numbers = list(map(int,input().split()))
        for i in numbers:
            print(i, end=' ')
        print(' ')