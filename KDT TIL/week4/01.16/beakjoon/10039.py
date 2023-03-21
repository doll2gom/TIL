a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

S = [a, b, c, d, e]
i = 0
for n in S:
    if n < 40:
        i += 40
    elif n >= 40:
        i += n
print(i//len(S))