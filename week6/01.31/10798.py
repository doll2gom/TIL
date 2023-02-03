'''
문제
다섯 개의 단어를 세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다. 
오른쪽으로 한 자리씩 이동 하면서 동일한 자리의 글자들을 세로로 읽어 나간다. 
해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다. 

입력
총 다섯줄의 입력이 주어진다. 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다.

출력
세로로 읽은 순서대로 공백 없이 출력한다. '''

import sys
sys.stdin = open("input.txt", "r")
from itertools import zip_longest

lst =[]
trans_words = []

# 리스트 컴프리헨션으로 5줄 행렬을 입력받는다.
words = [ list(map(str,input().split())) for _ in range(5)]
# 행 반복문
for w in words:
    # 15만큼 반복문을 만든다.
    # zip_longest함수를 사용해 각 위치의 인덱스 값과 함께 튜플로 변환
    # (0,'A'),(1,'a'),...,(5,None) ,...,(14, None)
    for w2 in zip_longest(range(15), w[0], fillvalue=None):
        # 만약 뒷자리 문자가 None이 아니면 리스트에 추가
        if w2[1] != None:
            lst.append(w2)
print(lst)
# 15번 반복문 # 리스트 내용 반복문
# 각 튜플의 앞자리가 맞으면 뒷자리 문자를 새로운 리스트에 추가 > 출력
for n in range(15):
    for l in lst:
        if l[0] == n:
            trans_words.append(l[1])
print(*trans_words,sep='')


'''
# 창조님 풀이
WORDS_NUM = 5

def print_transpose(lst2_):
    ans = ""
    
    for i in range(max([len(word) for word in lst2_])):
        for j in range(WORDS_NUM):
            if i < len(lst2_[j]):
                ans += lst2_[j][i]
                
    print(ans)


# input
word_lst2 = []
for _ in range(WORDS_NUM):
    word_lst2.append(sys.stdin.readline().strip())
    
print_transpose(word_lst2)
'''


# Aa0aPAf985Bz1EhCz2W3D1gkD6x
# Aa0aPAf985Bz1EhCz2W3D1gkD6x
'''
# [zip](https://docs.python.org/ko/dev/library/functions.html#zip)
# [zip_longest](https://docs.python.org/ko/dev/library/itertools.html#itertools.zip_longest)
# [zip_longest](https://wellsw.tistory.com/152)
'''
"""
AABCDD
afzz  
09121
a8EWg6
P5h3kx
"""