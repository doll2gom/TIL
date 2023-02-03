a, b, c = list(map(int,input().split()))
list = [a, b, c]
if a == b == c:
    print(10000+a*1000)
elif a == b or b == c:
    print(1000+b*100)
elif b == c or c == a:
    print(1000+c*100)
else:
    print(max(list)*100)