'''
[1, 2, 3, 4, 5]
 0  1  2  3  4
-5 -4 -3 -2 -1
'''
# N : 길이(5)
# n : shift
# n == 1 : [5, 1, 2, 3, 4]  > 인덱스 4부터(= N-n부터), 인댁스 4까지(N-n)
# n == 2 : [4, 5, 1, 2, 3]
# n == 3 : [3, 4, 5, 1, 2]
# n == 4 : [2, 3, 4, 5, 1]



a = [1, 2, 3, 4, 5]
N = len(a)


n = 2
new_a = [None for _ in range(N)]
for i in range(N):
    print (a, new_a) 
    for i in range (N) :
    # 새로운 리스트에
        print((i+n)%N)
        new_a[ (i+n)%N] = a[i]
    print (new_a)
for n in range(5):
    print(a[-n:] + a[:-n])