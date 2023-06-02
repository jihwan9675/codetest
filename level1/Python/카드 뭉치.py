def solution(cards1, cards2, goal):
    answer = ''
    
    idx_cd1 = 0
    idx_cd2 = 0
    
    for p in goal:
        flag= False
        if idx_cd1 < len(cards1):
            if cards1[idx_cd1] == p:
                idx_cd1 += 1
                flag = True
        if idx_cd2 < len(cards2):
            if cards2[idx_cd2] == p:
                idx_cd2 += 1
                flag = True
        if flag == False:
            return "No"
        
    return "Yes"
