from collections import defaultdict

N = int(input())

dic = defaultdict(int)

for i in range(N):
    dic[input()] += 1

temp = 0
answer = ''
for p in dic:
    if dic[p] > temp:
        temp = dic[p]
        answer = p
    elif dic[p] == temp:
        if answer > p:
            answer = p
        
            
print(answer)
