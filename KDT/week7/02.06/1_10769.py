'''  10769번 행복한지 슬픈지
문제
이모티콘은 세 개의 문자가 붙어있는 구조로 이루어져 있으며, 
행복한 얼굴을 나타내는 :-) 와 
슬픈 얼굴을 나타내는 :-( 가 있다.
입력
첫 줄에 최소 1개에서 최대 255개의 문자들이 입력된다.
출력
어떤 이모티콘도 있지 않으면, none
행복한 이모티콘과 슬픈 이모티콘의 수가 동일하게 있으면, unsure
행복한 이모티콘이 슬픈 이모티콘보다 많이 있으면, happy
슬픈 이모티콘이 행복한 이모티콘보다 많이 있으면, sad'''

import sys
sys.stdin = open("input.txt", "r")

# 문자열 입력받기
message = str(input())

# 이모티콘 2개 문자열 정의
good = ':-)'
bad = ':-('

# 갯수를 확인할 카운트 함수 정의
good_cnt = 0
bad_cnt = 0

# 문자열 길이만큼 반복
for s in range(len(message)):
	if message[s] == '-':	# 인덱스로 활용하여 가운데 문자'-'가 있다면 슬라이싱
		if good in message[s-1:s+2]:	
			good_cnt += 1	# good 슬라이싱 구간에 포함되어 있다면 카운드
		elif bad in message[s-1:s+2]:
			bad_cnt += 1	# bad 슬라이싱 구간에 포함되어 있다면 카운드

if good_cnt == 0 == bad_cnt: 
	print('none')
elif good_cnt > bad_cnt:
	print('happy')
elif good_cnt < bad_cnt:
	print('sad')
elif good_cnt == bad_cnt:
	print('unsure')