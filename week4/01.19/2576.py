import sys
sys.stdin = open("input.txt", "r")

# 빈 list 준비
N_list = []

# 7번의 입력을 받는다.
for n in range(0,7):
    N = int(input())
    # 입력값이 홀수라면 리스트에 추가
    if N % 2 != 0:
        N_list.append(N)
        
# 만약 리스트가 비어있다면 -1 출력
if N_list == []:
    print(-1)
else:
    print(sum(N_list))
    print(min(N_list))