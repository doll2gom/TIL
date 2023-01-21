T = int(input()) # 테스트 케이스 수
print(T)
for t in range(1, T+1):
    N = int(input()) # 입력 줄 수
    print(N)
    for s in range(1, N+1):
        numbers = list(map(int,input().split()))
        for i in numbers:
            print(i, end=' ')
        print('')