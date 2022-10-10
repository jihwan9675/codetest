def solution(X, Y):
    answer = ''
    _Xcount = [0,0,0,0,0,0,0,0,0,0]
    _Ycount = [0,0,0,0,0,0,0,0,0,0]
    
    for i in range(len(Y)):
        _Ycount[int(Y[i])] += 1
    
    for i in range(len(X)):
        _Xcount[int(X[i])] += 1

    for i in range(10):
        if _Xcount[i] > _Ycount[i]:
            _Xcount[i] = _Ycount[i]
            
    if sum(_Xcount) == 0:
        return "-1"
    if sum(_Xcount[1:]) == 0 & _Xcount[0] >= 0:
        return "0"
    
    for i in range(10):
        answer += str(9-i) * _Xcount[9-i]
    
    return answer
    
