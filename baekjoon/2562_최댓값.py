ls = []

for i in range(9):
    ls.append([int(input()),i+1])
    
ls.sort(key=lambda x:x[0])

print(ls[-1][0])
print(ls[-1][1])
