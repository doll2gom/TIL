lst = set()
for a in range(0,10):
    N = int(input())
    n = N%42
    lst.add(n)
print(len(lst))