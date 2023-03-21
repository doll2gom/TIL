''' 17826번 나의 학점은?
문제
A+: 1~5등
A0: 6~15등
B+: 16~30등
B0: 31~35등
C+: 36~45등
C0: 46~48등
F: 49~50등
프로그램을 통해 자신의 학점을 알아보고자 한다.

입력
첫째 줄에는 홍익이의 점수를 포함한, 학생들의 점수 50개가 띄어쓰기로 구분되어 주어진다.
점수는 내림차순으로 정렬되어있고, 같은 점수는 존재하지 않는다.

둘째 줄에는 홍익이가 받은 점수, 모든 점수는 0 이상 300 이하의 정수이다.

출력
학점을 출력하시오.'''
import sys
scores = list(map(int, sys.stdin.readline().split()))
myscore = int(sys.stdin.readline())
if myscore in scores[0:5]:
    print('A+')
elif myscore in scores[5:15]:
    print('A0')
elif myscore in scores[15:30]:
    print('B+')
elif myscore in scores[30:35]:
    print('B0')
elif myscore in scores[35:45]:
    print('C+')
elif myscore in scores[45:48]:
    print('C0')
else:
    print('F')
