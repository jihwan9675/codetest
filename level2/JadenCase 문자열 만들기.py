def solution(s):
    answer = ''
    ls = s.lower().split(' ')
    
    for i in range(len(ls)):
        if ls[i] != '' and not ls[i][0].isdigit():
            ls[i] = ls[i][0].upper() + ls[i][1:]
            
    return ' '.join(ls)
