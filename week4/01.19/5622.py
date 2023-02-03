import sys
sys.stdin = open("input.txt", "r")

# # 아스키코드 사용하여 A~Z까지 불러옴
# an = ord('A')
# az = ord('Z')+1

# # 알파벳 리스트로 만들어 관리
# ABC= [(chr(ask)) for ask in range(an,az)]

# # Dial 딕셔너리를 만들어 각 알파벳에 값을 입력해준다.
# Dial ={}
# val = 3
# ran = 0
# while True:
#     for a in range(0,len(ABC)):
#         for key in ABC[ran*3:ran*3+3]:
#                 Dial[key] = val
#         ran += 1
#         val += 1
#     break
# lsst = ['S', 'V', 'Y', 'Z']
# new_dict ={}
# for d in ABC:
#     if d in lsst:
#         Dial[d] = Dial.get(d)-1

# D = {'A': 3, 'B': 3, 'C': 3, 'D': 4, 'E': 4, 'F': 4, 'G': 5, 'H': 5, 'I': 5, 'J': 6, 'K': 6, 'L': 6, 'M': 7, 'N': 7, 'O': 7, 'P': 8, 'Q': 8, 'R': 8, 'S': 8, 'T': 9, 'U': 9, 'V': 9, 'W': 10, 'X': 10, 'Y': 10, 'Z': 10}

# A_dict = {}
# A = str(input())
# lA = int(len(A))

# for a in range(0,lA):
#     key = A[a]
#     val = Dial.get(A[a])
#     # 입력값A의 a번째 글자가 Dial에 있으면
#     if A[a] in A_dict:
#         A_dict[key] += int(val)
#     else:
#         if A[a] in Dial:
#             # 딕셔너리에 저장
#             A_dict[key] = int(val)
# print(sum(A_dict.values()))

D = {'A': 3, 'B': 3, 'C': 3, 'D': 4, 'E': 4, 'F': 4, 'G': 5, 'H': 5, 'I': 5, 'J': 6, 'K': 6, 'L': 6, 'M': 7, 'N': 7, 'O': 7, 'P': 8, 'Q': 8, 'R': 8, 'S': 8, 'T': 9, 'U': 9, 'V': 9, 'W': 10, 'X': 10, 'Y': 10, 'Z': 10}

A = str(input())
A_lst = []

for a in A:
    if a in D.keys():
        A_lst.append(D.get(a))
print(sum(A_lst))