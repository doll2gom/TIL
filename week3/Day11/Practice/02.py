a = map(str,input().split())
w = {}
for i in a:
    if i not in w:
        w[i] = 1
        # print(i, w[i])
    elif i in w:
        w[i] += 1
    print(i, w[i])