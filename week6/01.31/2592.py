'''문제
열 개의 자연수 평균과 최빈값

입력
첫째 줄부터 열 번째 줄까지 한 줄에 하나씩 자연수가 주어진다. 

출력
첫째 줄에는 평균을 출력하고, 
둘째 줄에는 최빈값을 출력한다.
최빈값이 둘 이상일 경우 그 중 하나만 출력한다. 
평균과 최빈값은 모두 자연수이다.'''

import sys
sys.stdin = open("input.txt", "r")

# class collections.Counter([iterable-or-mapping])
# 요소가 딕셔너리 키로 저장되고 개수가 딕셔너리값으로 저장되는 컬렉션
from collections import Counter

numbers = [ int(input()) for _ in range(10)]
print(sum(numbers)//10)
# most_common([n])
# n 개의 가장 흔한 요소와 그 개수를 가장 흔한 것부터 가장 적은 것 순으로 나열한 리스트를 반환
print(Counter(numbers).most_common(1)[0][0])

'''
# 상현님 풀이
# 2592 대표값
# mport sys
# sys.stdin = open("input.txt")

N_list = []
for i in range(10):
    N = int(input())
    N_list.append(N)

# print(N_list)
print(int(sum(N_list)/10))

temp = {}
for j in N_list:
    if j in temp:
        temp[j] = 1
    else:
        temp[j] = 1
print(j, temp)
max_li = temp.values()
most = 0
for x in temp:
    if temp[x] == max(max_li):
        most += x
#print(temp)
#print(max_li)
print(most)
'''