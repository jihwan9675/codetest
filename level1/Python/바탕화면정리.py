def solution(wallpaper):
    answer = [0,0,0,0]
    
    check = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                check.append([i,j])
    
    check.sort(key=lambda x : x[0])
    answer[0] = check[0][0]
    answer[2] = check[-1][0] + 1
    check.sort(key=lambda x : x[1])
    answer[1] = check[0][1]
    answer[3] = check[-1][1] + 1
    
    return answer
