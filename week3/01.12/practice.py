# 1~3의 세제곱의 결과가 담긴 리스트를 만드시오.

list = []
for i in range(1, 4):
    list.append(i**3)
print(list)

list = [i**3 for i in range(1,4)]
print(list)



numbers = [2, 4]
# 2로 나눈 몫으로만 구성된
# [1, 2]
def div_2(n):
    return n//2
print (list(map (div_2, numbers)))
print(list (map(lambda n: n//2, numbers) ))
print([ n//2 for n in numbers])
new_numbers = []
for n in numbers:
    new_numbers.append(n//2)
print(new_numbers)