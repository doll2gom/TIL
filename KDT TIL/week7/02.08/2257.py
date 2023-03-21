''' 2257번 화학식량
문제
COOHHH는 CO2H3로 나타낼 수 있다.
CH(CO2H)(CO2H)(CO2H)는 CH(CO2H)3와 같이 나타낼 수 있다.

화학식량이란 그 화학식에 포함되어 있는 모든 원자들의 질량의 합을 말한다. 
H는 수소(Hydrogen), 질량은 1, C는 탄소(Carbon), 질량은 12, O는 산소(Oxygen), 질량은 16이다. 
물은 두 개의 수소 원자와 한 개의 산소 원자로 이루어져 물의 화학식량은 18이다.

입력
첫째 줄에 화학식이 주어진다. 화학식은 H, C, O, (, ), 2, 3, 4, 5, 6, 7, 8, 9만으로 이루어진 문자열이며, 그 길이는 100을 넘지 않는다.

출력
첫째 줄에 화학식량을 출력한다. 분자량이 10,000이 넘는 고분자는 입력으로 주어지지 않는다.'''

import sys
sys.stdin = open("input.txt", "r")

weight = {
	'H': 1,
	'C': 12,
	'O': 16
}

# print(ord('9'))
# print(ord('C'))
# print(ord('('))

right = []
N = str(input())
print(N)

def askii(str):
	if ord(str) > 65:	# 아스키코드 65부터 알파벳 대문자
		return weight[str]	# 딕셔너리 키로 확용하여 값이 숫자를 리턴
	else:
		return int(str)	# 바로 숫자로 변환하여 리턴

def mult(list):
	a = 1
	for n in list:
		a *= n
	return a

ans = 1
numbers = []	# 괄호 안의 값을 넣는다.
big_numbers = []
for n in N:
	if n == ')':	# 괄호를 아스키 코드로 변환하면 안되기 때문에 먼저 확인한다.
		right.append(')')	# 괄호가 닫히면 괄호 안의 숫자들을 곱한다.
		print(n,'ans :',mult(numbers))
		numbers.clear()
	elif n =='(':	# 괄호를 아스키 코드로 변환하면 안되기 때문에 먼저 확인한다.
		if right == True:	# 아직 괄호 안에 있다면
			right.pop()
			numbers.append(ans)	# 괄호 안 리스트에 넣어두고 리스트를 비운다.
		else:
			big_numbers.append(ans)
		print('=====',numbers)
		ans = 1
		for num in numbers:
			big_numbers.append(num)
		numbers.clear()
	else:
		if right == True:
			if numbers == False:
				numbers.append(askii(n))
			else:
				for num in numbers:
					numbers *= num
				print(numbers)
				print(big_numbers)
		else:
			big_numbers.append(askii(n))	# 괄호 밖의 숫자라면 바로 최종리스트에 추가
		# print(numbers)
		# if numbers == False:	# 리스트가 비어있으면 넣는다.
		print(numbers)
		
		# if N[N.index(n)-1] == "(":
		# 	big_numbers.append(number)
		# 	print(numbers)
		# elif N[N.index(n)-1] == ")":
		# 	big_numbers.append(number)
		# 	print(numbers)
	print(numbers)

mlt = 1
for i in numbers:
	mlt *= i
print(mlt)
'''(H)2(O) // 18
CH(CO2H)3 // 148
((CH)2(OH2H)(C(H))O)3 // 222'''