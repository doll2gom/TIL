w = list(map(str,input().split()))
a = w[0]
b = w[1]
n = 0
for i in a:
    if i == b:
        n += 1
print(n)        