def solution(triangle):
    for i in range(1,len(triangle)):
        triangle[i-1].insert(0,0)
        triangle[i-1].append(0)
        for j in range(len(triangle[i])):
            sub = 0
            if triangle[i-1][j]>triangle[i-1][j+1]:
                sub = triangle[i-1][j]
            else:
                sub = triangle[i-1][j+1]
            triangle[i][j]+=sub
                    
    return max(triangle[-1])
