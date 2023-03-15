''' 11557번 Yangjojang of The Year
문제
학교별로 한 해동안 술 소비량이 주어질 때, 가장 술 소비가 많은 학교 이름을 출력하여라.

입력
입력의 첫 줄에는 테스트 케이스의 숫자 T가 주어진다.
매 입력의 첫 줄에는 학교의 숫자 정수 N(1 ≤ N ≤ 100)이 주어진다.

이어서 N줄에 걸쳐 학교 이름 S(1 ≤ |S| ≤ 20, S는 공백없는 대소문자 알파벳 문자열)와 해당 학교가 지난 한 해동안 소비한 술의 양 L(0 ≤ L ≤ 10,000,000)이 공백으로 구분되어 정수로 주어진다.
같은 테스트 케이스 안에서 소비한 술의 양이 같은 학교는 없다고 가정한다.

출력
각 테스트 케이스마다 한 줄에 걸쳐 술 소비가 가장 많은 학교의 이름을 출력한다.'''
import sys
for _ in range(int(sys.stdin.readline())):
    a, b = 0, 0
    for _ in range(int(sys.stdin.readline())):
        name, num = sys.stdin.readline().split()
        num = int(num)
        if b < num:
            a, b = name, num
        else:
            pass
    print(a)
