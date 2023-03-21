'''10828번 스택
push X: 정수 X를 스택에 넣는 연산이다.
pop:    가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
        정수가 없는 경우에는 -1을 출력한다.
size:   스택에 들어있는 정수의 개수를 출력한다.
empty:  스택이 비어있으면 1, 아니면 0을 출력한다.
top:    스택의 가장 위에 있는 정수를 출력한다. 
        스택에 정수가 없는 경우에는 -1을 출력한다.

입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.'''
import sys
# sys.stdin = open("input.txt", "r")

def stack_check(s):
    if s == 'pop':
        if len(stack) == 0:
            return -1
        else:
            return stack.pop()

    elif s == 'top':
        if len(stack) == 0:
            return -1
        else:
            return stack[-1]
stack = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    command = sys.stdin.readline().rstrip()

    if command[0:4] == 'push':
        stack.append(int(command[5:]))

    elif command == 'pop':
        print(stack_check('pop'))

    elif command == 'size':
        print(len(stack))
    
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)    

    elif command == 'top':
        print(stack_check('top'))

# stack = []

# def stack_check(str):
#     # pop: 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
#     # 1 정수있음 >> 가장 마지막에 넣은 수를 삭제하고 출력
#     # 2 정수없음 >> -1
#     if str == 'pop':
#         if len(stack) == 0:
#             return -1
#         else:
#             return stack.pop()

#     # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 정수가 없는 경우에는 -1을 출력한다.
#     # 1 정수있음 >> 가장 마지막에 넣은 수를 출력
#     # 2 정수없음 >> -1
#     elif str == 'top':
#         if len(stack) == 0:
#             return -1
#         else:
#             return stack[-1]

# N = int(input())
# for _ in range(N):
#     command = input()

#     # push X: 정수 X를 스택에 넣는 연산이다.
#     if command[0:4] == 'push':
#         stack.append(int(command[5:]))

#     # pop: 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
#     # 1 정수있음 >> 가장 마지막에 넣은 수를 삭제하고 출력
#     # 2 정수없음 >> -1
#     elif command == 'pop':
#         print(stack_check('pop'))

#     # size: 스택에 들어있는 정수의 개수를 출력한다.
#     elif command == 'size':
#         print(len(stack))
    
#     # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
#     # 1 비어있음         >> 1
#     # 2 비어있지 않음     >> 0       
#     elif command == 'empty':
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)    

#     # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 정수가 없는 경우에는 -1을 출력한다.
#     # 1 정수있음 >> 가장 마지막에 넣은 수를 출력
#     # 2 정수없음 >> -1
#     elif command == 'top':
#         print(stack_check('top'))

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