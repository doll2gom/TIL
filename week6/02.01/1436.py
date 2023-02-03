''' 1436번 영화감독 숌
6이 적어도 3개이상 연속으로 들어가는 수
제일 작은 숫자는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... , N번째는 (N번째로 작은 숫자)

입력
첫째 줄에 숫자 N이 주어진다. N은 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 N번째 영화의 제목에 들어간 수를 출력'''

N = int(input())
# 첫 번째 숫자는 666이 된다.
num = 666
# 그래서 1번은 이미 카운트 되어있는 상태
cnt = 1
# cnt = 1

# 반복문으로 숫자 N 탐색
while True: 
    # 시작 숫자 num을 문자열 s_num으로 변환
    s_num = str(num) 
    # 문자열s_num에 문자열 666이 포함되어 있는지 찾는다.
    if '666' in s_num: 
        # 여기서 카운트 수와 N이 같다면 break
        # 이미 카운트는 +1되어 있음
        if cnt == N: 
            break
        # 카운트에 1을 추가해 cnt번째 문자를 계속 찾아 나간다.
        # 처음부터 cnt = 1 이었기 때문에 문자를 찾는 순서는 1 앞서 있는 것이다.
        cnt += 1 
    # if 결과와 상관없이 계속 원래 숫자 num에 1을 더해간다.
    num += 1 
# N번째 숫자에서 멈췄기 때문에 숫자 num을 출력
print(num)

'''
2
1666

3
2666

6
5666

187
66666

500
166699'''

'''a = 3
N는 1 ~ 10,000까지
영화제목은 666 ~ ?까지 > while

def movie_title(N):
    while True:
        num = 666
        # num 숫자를 정수로 바꿔서 문자열 '666'이 들어가는지 확인
        s_num = str(num)
        M = len(s_num)
        cnt = 1
        if cnt == N:
            break
        for i in ):
            if s_num[i] == s_num[i+1] == ] == 6:
                cnt += 1
                num += 1
            else:
                num += 1
    return cnt
    #     # 만약 666이 나온 횟수 cnt와 input값이 같다면 break
    #     if cnt == input:
    #         break
    #     # 문자열에 666이 포함되어 있다면 카운드하고 계속 숫자를 1씩 더해간다.
    #     cnt += 1
    # num += 1
print(movie_title(a))


n = 5
m = 21
cards = [5, 6, 7, 8, 9]
def blackjack(N,M,cards):
    max_total = 0
    for i in ):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                total = cards[i] + cards[j] + cards[k]

                if max_total < total <= M:
                    max_total = total
                
                if total == M:
                    return total
    # return max_total
print(blackjack(n,m,cards))'''

