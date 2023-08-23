N, X = map(int, input().split())
ls = list(map(int, input().split()))

for i in range(len(ls)):
    if ls[i]<X:
        print(ls[i], end=' ')
        
