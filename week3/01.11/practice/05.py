T = int(input()) # 테스트 케이스 수
for t in range(1, T+1):
    print(T)
    N = int(input()) # 입력 줄 수
    print(N)
    for s in range(1, N+1):
        S = list(map(str,input().split()))
        for sent in S:
            print(sent, end=' ')
        print('')