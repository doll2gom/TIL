'''1063번 킹
문제
8*8크기의 체스판 알파벳은 열을 상징하고, 숫자는 행을 상징한다. 
왼쪽 열 A, 오른쪽 열 H까지 , 
행은 아래부터 위까지 1~8

R : 한 칸 오른쪽으로 
L : 한 칸 왼쪽으로
B : 한 칸 아래로
T : 한 칸 위로
RT : 오른쪽 위 대각선으로
LT : 왼쪽 위 대각선으로
RB : 오른쪽 아래 대각선으로
LB : 왼쪽 아래 대각선으로

돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 아래 그림을 참고하자.

입력으로 킹이 어떻게 움직여야 하는지 주어진다. 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.

킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 킹의 위치, 돌의 위치, 움직이는 횟수 N이 주어진다. 둘째 줄부터 N개의 줄에는 킹이 어떻게 움직여야 하는지 주어진다. N은 50보다 작거나 같은 자연수이고, 움직이는 정보는 위에 쓰여 있는 8가지 중 하나이다.

출력
첫째 줄에 킹의 마지막 위치, 둘째 줄에 돌의 마지막 위치를 출력한다.'''

import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint
Y = ['A','B','C','D','E','F','G','H']
dict1 = {'A','B','C','D','E','F','G','H'}
# 이동 명령어 
delta = {
'R' : (0,1),
'L' : (0,-1),
'B' : (-1,0),
'T' : (1,0),
'RT' : (-1,1),
'LT' : (-1,-1),
'RB' : (1,1),
'LB' : (1,-1)}

check = [ [(x, y) for y in range(8)] for x in range(8)]
pprint(check)

# 킹,돌,이동횟수
K, S, n = input().split()
N = int(n)
print(K, S, N)

# 아스키코드로 'A'는 65
# x좌표 즉 행은 숫자로 8까지 표기되어 있기 가장 위의 행은 x좌표가 8-8로 0이 나온다. 
kx, ky = 8 - int(K[1]), ord(K[0]) - ord('A')
sx, sy = 8 - int(S[1]), ord(S[0]) - ord('A')
print(dict1)

for _ in range(N):
    go = str(input())

    for i in range(8):
        x = 8 - i
        for j in range(8):
            y = 8 - j
        print(x,y)
    print(go)
pprint.pprint(delta)

"""
창조님 풀이
import sys


def print_problem_info(str1, str2):
    print(f"\033[95m# {str1}. \x1b[96m{str2}\033[00m")


list_var = [0 for i in range(6)]
list_var = [17608, 7568, 1063]
dict_var = {
    list_var[0] : "막대기",
    list_var[1] : "덩치",
    list_var[2] : "킹",
}

dict_var = dict(sorted(dict_var.items()))


while True:
    print("===아래 리스트에서 문제 번호 선택!===")
    for k, v in dict_var.items():
        print(f"\u001b[90m{k}. {v}\033[0m")

    try:
        problem_num = int(input("\n문제 번호 입력 > "))
    except:
        print("Terminated!")
        break
    
    if problem_num == list_var[0]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        ## input
        n_num = int(sys.stdin.readline())

        num_lst = []
        for _ in range(n_num):
            num_lst.append(int(sys.stdin.readline()))
            

        ## solution
        def get_stick_num(lst_: list):
            ''' get_stick_num(list)
            # Description
            Counts the number of sticks which can watch on right-side
            
            # argument
            lst_    : list, heights of sticks
            
            # return
            int     : number of sticks which can watch on right-side
            '''
            max_height = 0
            ans = 0
            
            ## Visit list in reverse
            for stick in lst_[::-1]:
                ## Renew if stick is bigger than maximun ex-stick
                ## And count plus
                if stick > max_height:
                    max_height = stick
                    ans += 1
                    
            ## return count
            return ans


        ## print
        print(get_stick_num(num_lst))
        ####################
    
    
    
    
    
    elif problem_num == list_var[1]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        ## input
        people_num = int(sys.stdin.readline())

        people_info_lst = []
        for _ in range(people_num):
            people_info_lst.append(tuple(map(int, sys.stdin.readline().split())))
            
        # print(people_info_lst)

        ## solution
        def get_size_order(lst_: list):
            ''' get_size_order(list)
            # Description
            Calculate size ranking and return result
            Size ranking is 'greater count + 1' -> greater count: number of people who have greater weight and height.
            
            # argument
            lst_    : list, Information of people as tuple (weight: int, height: int) in list
            
            # return
            list    : Size ranking
            '''
            ## Dictation removes duplication
            ## Choose list
            ans_lst = []
            
            for i in range(len(lst_)):
                cnt = 1
                ## Compare and count greater size people num
                for info in lst_:
                    ## Compare size
                    if info[0] > lst_[i][0] and info[1] > lst_[i][1]:
                        ## Add greater size people num
                        cnt += 1
                ## Append count in list
                ans_lst.append(cnt)
                
            return ans_lst


        ## print
        print(*get_size_order(people_info_lst))
        ####################
    
    
    
    
    
    elif problem_num == list_var[2]:
        print_problem_info(problem_num, dict_var[problem_num])
        
        
        #################### solution code
        ## initialize
        BOARD_SIZE = 8

        movement_dict = {
            "R": (1, 0),
            "L": (-1, 0),
            "T": (0, 1),
            "B": (0, -1),
            "RT": (1, 1),
            "LT": (-1, 1),
            "RB": (1, -1),
            "LB": (-1, -1),
        }

        ## input
        # board_lst = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        king_pos, rock_pos, move_num = sys.stdin.readline().split()

        move_lst = []
        for _ in range(int(move_num)):
            move_lst.append(sys.stdin.readline().strip())
            
            
        ## solution
        def is_in_board(n1: int, n2: int):
            ''' is_in_board(int, int)
            # Description
            Check if piece is in board after movement
            
            # argument
            n1  : int, location of x(column)
            n2  : int, location of y(row)
            
            # return
            bool    : True if in board else False
            '''
            return True if 0 <= n1 < BOARD_SIZE and 0 <= n2 < BOARD_SIZE else False
            
        def get_location(pos1: str, pos2: str, lst_: list):
            ''' get_location(str, str, list)
            # Description
            Input location of king and rock in chess board and movements of king
            
            # argument
            pos1    : str, location of king
            pos2    : str, location of rock
            lst_    : list, movement of king
            
            # return
            str     : location of king as chess-format(A1 ~ H8)
            str     : location of rock as chess-format(A1 ~ H8)
            '''
            p1 = ("ABCDEFGH".index(pos1[0]), "12345678".index(pos1[1]))
            p2 = (ord(pos2[0]) - ord('A'), int(pos2[1]) - 1)
            
            print(p1, p2)
            
            for move in lst_:
                new = (p1[0] + movement_dict[move][0], p1[1] + movement_dict[move][1])
                new2 = p2   ## Rock stays if king doesn't touch it
                
                print(new)
                if not is_in_board(new[0], new[1]):
                    continue
                
                ## Check rock location
                if new[0] == new2[0] and new[1] == new2[1]:
                    new2 = (p2[0] + movement_dict[move][0], p2[1] + movement_dict[move][1])
                    
                    if not is_in_board(new2[0], new2[1]):
                        continue
                
                p1 = new    ## Move king
                p2 = new2   ## Move rock
                # print(p1, p2)
                
            return ("ABCDEFGH"[p1[0]]+"12345678"[p1[1]], "ABCDEFGH"[p2[0]]+"12345678"[p2[1]])
            

        ## print
        print(*get_location(king_pos, rock_pos, move_lst), sep="\n")
        ####################
        
        
        
        
        
    else:
        print("Terminated!")
        break


    print()
"""