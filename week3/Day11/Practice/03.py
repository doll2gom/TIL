a = list(map(str,input()))
for i in a:
    if i == 'e':
        a.remove('e')
str = ''.join(a)
print(str)