a = list(map(str,input()))
n = -1
for i in a:
    if 'e' in a:
        n += 1
        if i != 'e':
            continue
        else:
            print(n)
    elif 'e' not in a:
        print(n)
        break        