'''
문제
두 집합 A와 B가 있다. 
두 집합의 대칭 차집합의 원소의 개수를 출력
두 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.

A = { 1, 2, 4 } 이고, 
B = { 2, 3, 4, 5, 6 } 라고 할 때,  
A-B = { 1 } 이고, 
B-A = { 3, 5, 6 } 이므로, 
대칭 차집합의 원소의 개수는 1 + 3 = 4개이다.

입력
첫째 줄에 A의 개수와 B의 개수가 빈 칸을 사이에 두고 주어진다. 
둘째 줄에 A의 모든 원소가, 
셋째 줄에 B의 모든 원소가 빈 칸을 사이에 두고 각각 주어진다. 
각 집합의 원소의 개수는 200,000을 넘지 않으며, 모든 원소의 값은 100,000,000을 넘지 않는다.

출력
첫째 줄에 대칭 차집합의 원소의 개수를 출력한다.'''
# 해시, 트리 자료구조

import sys 
sys.stdin = open("input.txt", "r")
A, B  = map(int,input().split())
a  = set(map(int,input().split()))
b  = set(map(int,input().split()))

print(len(a|b)-len(a&b))