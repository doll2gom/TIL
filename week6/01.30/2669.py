'''
문제
평면에 네 개의 직사각형이 놓여 있는데 그 밑변은 모두 가로축에 평행하다. 이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고, 겹쳐 있을 수도 있고, 하나가 다른 하나를 포함할 수도 있으며, 변이나 꼭짓점이 겹칠 수도 있다.

이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.

입력
입력은 네 줄이며, 각 줄은 직사각형의 위치를 나타내는 네 개의 정수로 주어진다. 첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭짓점의 x좌표, y좌표이고 세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭짓점의 x좌표, y좌표이다. 모든 x좌표와 y좌표는 1이상이고 100이하인 정수이다.

출력
첫 줄에 네개의 직사각형이 차지하는 면적을 출력한다.
'''
import sys
sys.stdin = open("input.txt", "r")
import pprint
matrix = []
m_dict = {}
#x x,y 합집합 만들기 set
x_set = set()
y_set = set()
for _ in range(1,5):
    line = list(map(int,input().split()))
    matrix.append(line)
    print(line)
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]
    x = set()
    y = set()
    for i in range(x1, x2+1):
        x.add(i)
        x_set.add(i)
    for j in range(y1, y2+1):
        y.add(j)
        y_set.add(j)
    m_dict[_] = (x,y)
pprint.pprint(m_dict)
# for x_x in range(101):
    # for y_y in range(101):

for n1 in m_dict:
    for n2 in m_dict[n1]:
        # x_set_min = x_set[0]
        print(x_set[0])
        # if n2[0] < x_set_min:
        #     print(n2)

print(matrix)
print(x_set, y_set)



# (1,2,3,4,5,6),(1,2,3,4,5,6,7)
# (7,8),(3,4,5,6)
# (합집합 - 교집합) + (전체 교집합)
# A (1,2,3,4) (2,3,4)
# B (2,3,4,5) (3,4,5,6,7)
# C (3,4,5,6) (1,2,3,4,5)
# D (7,8) (3,4,5,6)




'''
import sys

def sol_set(lst_2d):
    ans = set()
    for lst_ in lst_2d:
        for x in range(lst_[0], lst_[2]):
            for y in range(lst_[1], lst_[3]):
                ans.add((x, y))
                
    return len(ans)


# input
pos_lst2 = []
for _ in range(4):
    pos_lst2.append(list(map(int, sys.stdin.readline().split())))

# print
print(sol_set(pos_lst2))
'''

