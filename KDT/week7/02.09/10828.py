'''10828번 스택
push X: 정수 X를 스택에 넣는 연산이다.
pop: 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
    정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.'''
import sys
sys.stdin = open("input.txt", "r")
from collections import deque

a = []
stack = deque(a)

# 정수가 있는지 확인하려고 만든 함수
def stack_type(list):
    lst = []
    cnt = 0
    for n in reversed(list):
        if isinstance(n,int) == True:
            cnt += 1
            lst.append(isinstance(n,int))
    if True in lst:
        return True
    else:
        return False

for command in range(int(input())):
    command = input()

    # push X: 정수 X를 스택에 넣는 연산이다.
    if command[0:4] == 'push':
        stack.append(int(command[-1]))

    # pop: 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
    # 1 스택이 비어있음 (= 정수 없음) >> -1
    # 2 스택에 비어있지 않음
        # 2-1 스택에 정수없음       >> -1
        # 2-2 스택에 정수있음       >> 그 수를 삭제하고 출력
    elif command == 'pop':
        for n in reversed(stack):
            print('pop')
            if isinstance(n,int) == True:
                print(n)        # ??????
                print(stack)
                a = stack.remove(n)
                print(stack)
                print(a)
                pass
            else:
                print(-1)

    # size: 스택에 들어있는 정수의 개수를 출력한다.
    # 1 스택이 비어있음 (= 정수 없음) >> -1
    # 2 스택에 비어있지 않음
        # 2-1 스택에 정수없음       >> -1
        # 2-2 스택에 정수있음       >> 그 수를 삭제하고 출력
    elif command == 'size':
        print(len(stack))
    
    # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    # 1 스택이 비어있음         >> 1
    # 2 스택에 비어있지 않음     >> 0       
    elif command == 'empty':
        if stack == False:
            print(1)
        else:
            print(0)    

    # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 정수가 없는 경우에는 -1을 출력한다.
    # 1 스택이 비어있음 (= 정수 없음) >> -1
    # 2 스택에 비어있지 않음
        # 2-1 스택에 정수없음       >> -1
        # 2-2 스택에 정수있음       >> 마지막 위치의 정수 출력
    elif command == 'top':
        if stack == False:
            print(-1)
        else:
            print(stack[-1])

'''
14
push +1
push +2
top
size
empty
pop
pop
pop
size
empty
pop
push +3
empty
top'''
# 2
# 2
# 0
# 2
# 1
# -1
# 0
# 1
# -1
# 0
# 3
'''
7
pop
top
push 123
top
pop
top
pop'''
# -1
# -1
# 123
# 123
# -1
# -1