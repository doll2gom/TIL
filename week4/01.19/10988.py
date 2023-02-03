word = 'level'
print(int(word == word[::-1]))

# 1 Input
# 2 
start = 0
end = 0

T1 = 'level'
print(T1)
while True:
    for n in range(0,len(T1)-1):
        if T1[n] == T1[n+(-1)]:
            pass
            print(1)
            break
        else:
            break