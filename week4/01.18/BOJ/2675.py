import sys
sys.stdin = open("input.txt", "r")

# 빈 리스트와 QR을 문자열로 준비
P = []
QR = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:'

T = int(input())
for t in range(0,T):
    R, S = input().split()
    # 정수R, 문자열S를 입력받아 타입을 따로 정해준다.
    R = int(R)
    S = str(S)
    # 문자열S의 길이(len(S)) 만큼 반복문
    for r in S[:]:
        # 문자열QR을 반복문으로 
        if r in QR:
            print(r*R,end='')
    print()