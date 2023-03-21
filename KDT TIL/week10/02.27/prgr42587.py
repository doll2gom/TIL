
'''프린터
문제 설명
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.

내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.

현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

제한사항
현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.
입출력 예
priorities	location	return
[2, 1, 3, 2]	2	1
[1, 1, 9, 1, 1, 1]	0	5'''


from collections import deque

def solution(priorities, location):
    answer = 0
    loc = location
    Q = deque(priorities)
    while True:
        m = max(Q)
        if Q[0] < m:
            Q.rotate(-1) # 왼쪽으로 하나씩 이동
            loc -= 1
        elif Q[0] == m:
            Q.popleft()
            answer += 1
        if loc == 0:
            answer += 1
            return answer
            break
        elif priorities[location] == len(Q):
            return answer
            break

print(solution([1, 1, 9, 1, 1, 1], 0)) # 5
print(solution([2, 1, 3, 2], 2)) # 1
print(solution([1, 2, 3, 4, 5, 6], 0))  # 5

# 런타임 에러

from collections import deque

# priorities [1, 1, 9, 1, 1, 1]
# location 0
def solution(priorities, location):

    '''@enumerate(iterable) 내장함수: (인덱스값, 요소)를 튜플 형식으로 돌려줌'''
    # [(0,1), (1,1), (2,9), (3,1), (4,1), (5,1)]
    printer = [ (i,p) for i,p in enumerate(priorities)]
    answer = 0

    while printer: # printer에 요소가 남지 않을 때까지 반복한다.
        first = printer.pop(0) # 맨 앞에 있는 요소부터 확인한다. # (0,1)

        ''' any(iterable) 내장함수: 입력받은 요소에서 하나라도 참이면 True'''
        # printer에서 요소를 하나씩 꺼내오는데,
        # 맨 앞에 있는 요소보다 높은 수가 하나라도 있다면(True)
        # printer의 뒤에 넣는다.
        if any(first[1] < other[1] for other in printer):
            printer.append(first)

        # 맨 앞에 있는 요소가 제일 크다면(방금 pop한 요소가 제일 크다면)
        # 출력횟수를 카운트하여 +1 한다.
        else:
            answer += 1

            # pop한 뒤 [0]번 인덱스가 내가 찾는 값인지 확인하고 break
            if first[0] == location: 
                break
            
    return answer


print(solution([1, 1, 9, 1, 1, 1], 0)) # 5
print(solution([2, 1, 3, 2], 2)) # 1
print(solution([1, 2, 3, 4, 5, 6], 0))  # 6

def solution(priorities, location):
    printer = [ (i,p) for i,p in enumerate(priorities)]
    answer = 0
    while printer: # printer에 요소가 남지 않을 때까지 반복한다.

        first = printer.pop(0) # 맨 앞에 있는 요소부터 확인한다. # (0,1)

        if any(first[1] < other[1] for other in printer):
            printer.append(first)
        else:
            answer += 1
            if first[0] == location: 
                break
            
    return answer

# 런타임 에러