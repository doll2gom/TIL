a = int(input())
if a < 0:
    print(-1)
# a가 0보다 크면 반복한다.
else:
    result = 0
    # while 종료 조건은?
    while a > 0:
        # result는 계속 a를 10으로 나눈 몫으로 교체됨
        result += a%10
        # result는 나머지를 더해나감
        a //= 10
    print(result)


# solve 2
# n = input()
# result2 = 0
# for i in n:
#     result2 += int(i)
    
# print(result2)