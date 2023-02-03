'''
입력
총 다섯 개 줄에 각 참가자가 얻은 네 개의 평가 점수가 공백으로 구분되어 주어진다.

출력
첫째 줄에 우승자의 번호와 그가 얻은 점수를 출력한다.
'''
import sys
sys.stdin = open("input.txt", "r")
score_cnt = 0
winner = 0
matrix = [ list(map(int,input().split())) for _ in range(4)]
for line in matrix:
    score = sum(line)
    winner += 1
    if score > score_cnt:
        score_cnt = score
        
print(winner, score_cnt)