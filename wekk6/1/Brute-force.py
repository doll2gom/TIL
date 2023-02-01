# [리스트]를 for 문으로 range돌리며 M에서 마이너스한다.
# 결과를 절댓값으로 변환 abs()
# (절댓값, 원래숫자) 형식의 튜플로 생성 
# 정렬 > 가장 앞쪽에 위치한 3개 
'''M-[리스트]생성 >결과를 절댓값으로 변환 abs() > (절댓값, 원래숫자) 형식의 튜플로 생성 > 정렬한다 > 가장 앞쪽에 위치한 3개 구함'''\




'''for i in range(5):
    for j in range(5):
        for k in range(5):
            if i == j:
                pass
            if i == k:
                pass
            if j == k:
                pass
                print(i,j,k)'''
n = 5
m = 21
c = [5, 6, 7, 8, 9]
def blackjack(N,M,cards):
    max_total = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                total = cards[i] + cards[j] + cards[k]

                if max_total < total <= M:
                    max_total = total
                
                if total == M:
                    return total
    # return max_total
print(blackjack(n,m,c))

# O(N^3)
for i in range(5):
    for j in range(5):
        for k in range(5):
        # 1, 1, k => 비교문 필요
            pass
'''# O(N^3)
for i in range (N-2):
    for j in range(i+1, N-1) :
        for k in range(j+1,N):
            pass'''