N= int(input())
ls = list(map(int, input().split()))
ls.sort()
answer = 0
for i in range(N):
    answer += ls[i]/ls[-1]*100
print(answer/N)
