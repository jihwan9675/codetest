def solution(players, callings):
    dic = dict()
    
    for i in range(len(players)):
        dic[players[i]] = i
        
    for p in callings:
        temp = players[dic[p]-1]
        players[dic[p]-1] = players[dic[p]]
        players[dic[p]] = temp
        dic[p] -= 1
        dic[temp] +=1
    
    return players
