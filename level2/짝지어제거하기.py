def solution(s):
    idx = 0
    ls = []
    
    for p in s:
        if ls:
            if ls[-1] == p:
                del ls[-1]
            else:
                ls.append(p)
        else:
            ls.append(p)
    if ls:
        return 0
    return 1
