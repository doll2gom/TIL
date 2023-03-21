''' 2920번 음계
문제
1부터 8까지 ascending, 
8부터 1까지 descending, 
둘 다 아니라면 mixed 이다.

연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

입력
첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.

출력
첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.'''

import sys
sys.stdin = open("input.txt", "r")

ans = ['ascending', 'descending', 'mixed']
t = list(map(int, input().split()))
num = [ n for n in range(1,9)]
if t == num:
    print(ans[0])
elif t == num[::-1]:
    print(ans[1])
else:
    print(ans[2])