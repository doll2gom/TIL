import sys
sys.stdin = open("input.txt", "r")

S = str(input())
s = []
# 알파벳 문자를 아스키코드로 변환 하여 시작하는 수와 끝나는 수를 먼저 구한다
# print(ord('a'))
# print(ord('z'))

for n in range(97,123):
    if chr(n) in S:
        s.append(S.find(chr(n)))
print(*s)