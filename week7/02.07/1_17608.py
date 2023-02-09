''' 17608번 막대기
문제
왼쪽부터 차례로 번호를 붙인다. 각 막대기의 높이는 순서대로 6, 9, 7, 6, 4, 6 이다. 
일렬로 세워진 막대기를 오른쪽에서 보면 지금 보이는 막대기보다 뒤에 있고 높이가 높은 것이 보이게 된다. 
예를 들어, 그림과 같은 경우엔 3개(6번, 3번, 2번)의 막대기가 보인다.

N개의 막대기에 대한 높이 정보가 주어질 때, 오른쪽에서 보아서 몇 개가 보이는지를 알아내는 프로그램을 작성하려고 한다.

입력
첫 번째 줄에는 막대기의 개수를 나타내는 정수 N (2 ≤ N ≤ 100,000)이 주어지고 
N줄 각각에는 막대기의 높이를 나타내는 정수 h(1 ≤ h ≤ 100,000)가 주어진다.

출력
오른쪽에서 N개의 막대기를 보았을 때, 보이는 막대기의 개수를 출력한다.
'''

import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
	stack.append(int(input()))
cnt = 1
last = stack[-1]
for n in reversed(range(N)):
	if stack[n] > last:
		cnt += 1
		last = stack.pop(n)
print(cnt)