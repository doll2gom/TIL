# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제

'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
m31 = [1, 3, 5, 7, 8, 10, 12]
m30 = [4, 6, 9, 11]
for a in range(1, T + 1):
    t = input()
    if int(t[4:6]) in m31 and int(t[6:8]) > 31:
        print(f'#{a} -1')
    elif int(t[4:6]) in m30 and int(t[6:8]) > 30:
        print(f'#{a} -1')
    elif int(t[4:6]) == 2 and int(t[6:8]) > 28 :
        print(f'#{a} -1')
    elif int(t[4:6]) == 0 or int(t[6:8]) == 0 :
        print(f'#{a} -1')
    else:
        print(f'#{a} {t[0:4]}/{t[4:6]}/{t[6:8]}')
