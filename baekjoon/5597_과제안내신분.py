ls = [0]*30

for i in range(28):
    ls[int(input())-1] = 1
    
for i in range(30):
    if ls[i] == 0:
        print(i+1)
