import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(0,T):
    W = list(map(str,input().split()))
    # 빈 리스트 준비
    lst = []
    # 각 단어를 뒤집어 변환, 각각 리스트에 삽입을 반복한다.
    for w in W:
        rev_w = w[::-1]
        lst.append(rev_w)
    print(*lst)
        # print(w[::-1],end ='')