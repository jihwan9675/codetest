def solution(m, n, puddles):
    answer = 0
    ls = []
    for i in range(n+1):
        sub = []
        for j in range(m+1):
            sub.append(0) 
        ls.append(sub)
    for p in puddles:
        ls[p[1]][p[0]]=-1
    ls[1][0]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if ls[i][j]==-1:
                continue
            elif ls[i-1][j]==-1:
                ls[i][j]= ls[i][j-1]
            elif ls[i][j-1]== -1:
                ls[i][j] = ls[i-1][j]
            else:
                ls[i][j] = ls[i-1][j]+ls[i][j-1]
    
    return ls[n][m]%1000000007
