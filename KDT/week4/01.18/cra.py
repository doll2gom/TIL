ap = ['c=', 'c-','dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
for i in ap:
    s = s.replace(i,'X')
print(len(s))