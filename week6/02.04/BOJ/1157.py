''' 1157번 단어 공부
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.'''

import sys
sys.stdin = open("input.txt", "r")

A = input().upper()
A_list = list(set(A))
lst = []
for a in A_list:
    lst.append(A.count(a))
if lst.count(max(lst)) >= 2:
    print('?')
else:
    print(A_list[lst.index(max(lst))])